"""Offline query preparation and package validation. No QRadar connection."""
from __future__ import annotations
import datetime as dt
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r'<([A-Z_]+)>')
class ValidationError(ValueError):
    """Invalid local input; never an Ariel parser result."""

def _unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result

def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8-sig'), object_pairs_hook=_unique_pairs)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f'Cannot read JSON {path}: {exc}') from exc

def load_catalog(root=ROOT):
    items = read_json(Path(root) / 'queries.json') + read_json(Path(root) / 'variants.json')
    found = {}
    for item in items:
        ident = item.get('id')
        if not re.fullmatch(r'(Q[0-9]{3}|OPT[0-9]{2})', str(ident)) or ident in found:
            raise ValidationError(f'Invalid or duplicate query ID: {ident}')
        found[ident] = item
    return found

def _value(key, value, spec):
    if value is None or value == '':
        raise ValidationError(f'Missing parameter: {key}')
    kind = spec['type']
    if kind in ('integer', 'port'):
        if isinstance(value, bool) or not re.fullmatch(r'[0-9]+', str(value)):
            raise ValidationError(f'Integer required: {key}')
        number = int(value)
        upper = 65535 if kind == 'port' else 2**63 - 1
        if not 1 <= number <= upper:
            raise ValidationError(f'Value outside valid range: {key}')
        return str(number)
    if not isinstance(value, str):
        raise ValidationError(f'String required: {key}')
    if any(ord(c) < 32 for c in value) or any(c in value for c in "'\\<>"):
        raise ValidationError(f'Unsafe or ambiguous literal in {key}; prepare complex values manually')
    if kind == 'ipv4':
        try:
            ipaddress.IPv4Address(value)
        except ipaddress.AddressValueError as exc:
            raise ValidationError(f'IPv4 address required: {key}') from exc
    elif kind == 'cidr4':
        try:
            ipaddress.IPv4Network(value, strict=False)
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError) as exc:
            raise ValidationError(f'IPv4 CIDR required: {key}') from exc
    elif kind == 'hostname':
        if len(value) > 253 or not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?', value):
            raise ValidationError(f'Hostname required: {key}')
        if any(not label or len(label) > 63 or label.startswith('-') or label.endswith('-') for label in value.split('.')):
            raise ValidationError(f'Invalid hostname labels: {key}')
    elif kind == 'datetime':
        try:
            dt.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        except ValueError as exc:
            raise ValidationError(f'Date format yyyy-MM-dd HH:mm:ss required: {key}') from exc
    return value

def render(ident, params, root=ROOT):
    if not isinstance(params, dict):
        raise ValidationError('Parameters must be a JSON object')
    catalog = load_catalog(root)
    if ident not in catalog:
        raise ValidationError(f'Unknown query ID: {ident}')
    schema = read_json(Path(root) / 'parameter_schema.json')
    sql = catalog[ident]['sql']
    keys = set(PLACEHOLDER.findall(sql))
    values = {}
    for key in sorted(keys):
        if key not in schema:
            raise ValidationError(f'No parameter schema for: {key}')
        values[key] = _value(key, params.get(key), schema[key])
    if {'START', 'STOP'} <= keys:
        begin = dt.datetime.strptime(values['START'], '%Y-%m-%d %H:%M:%S')
        end = dt.datetime.strptime(values['STOP'], '%Y-%m-%d %H:%M:%S')
        if end <= begin:
            raise ValidationError('STOP must be later than START')
    # Substitute in one pass. Inserted values are never reprocessed as templates.
    rendered = PLACEHOLDER.sub(lambda match: values[match.group(1)], sql)
    return rendered + '\n'

def write_output(path, text, force=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation preserves an existing output unless explicitly overridden.
    if not force:
        try:
            with path.open('x', encoding='utf-8', newline='\n') as stream:
                stream.write(text)
        except FileExistsError as exc:
            raise ValidationError(f'Output exists; choose another path or use --force: {path}') from exc
        return
    handle, temp = tempfile.mkstemp(prefix='.' + path.name + '.', dir=path.parent)
    try:
        with os.fdopen(handle, 'w', encoding='utf-8', newline='\n') as stream:
            stream.write(text)
        os.replace(temp, path)
    finally:
        Path(temp).unlink(missing_ok=True)

def query_file_text(item):
    return f"-- {item['id']} / {item['title']}\n-- Offline template: map Hunt_* and replace <...>.\n\n{item['sql']}\n"

def validate_catalog(root=ROOT):
    root = Path(root)
    catalog = load_catalog(root)
    expected = {f'Q{i:03}' for i in range(1, 111)} | {f'OPT{i:02}' for i in range(1, 8)}
    if set(catalog) != expected:
        raise ValidationError('Expected Q001-Q110 and OPT01-OPT07')
    schema = read_json(root / 'parameter_schema.json')
    references = {x['id'] for x in read_json(root / 'sources.json')}
    for ident, item in catalog.items():
        sql = item.get('sql', '')
        if not sql.startswith('SELECT ') or any(c in sql for c in '“”‘’'):
            raise ValidationError(f'Invalid query text: {ident}')
        if set(PLACEHOLDER.findall(sql)) - set(schema):
            raise ValidationError(f'Unknown placeholders: {ident}')
        if 'TEXT SEARCH' in sql and re.search(r'\bOR\b', sql):
            raise ValidationError(f'TEXT SEARCH combined with OR: {ident}')
        refs = {s.strip() for s in item.get('refs', '').split(',') if s.strip()}
        if refs - references:
            raise ValidationError(f'Unknown references: {ident}')
        target = root / 'queries' / (ident + '.aql')
        if not target.is_file() or target.read_text(encoding='utf-8') != query_file_text(item):
            raise ValidationError(f'Query file/catalog mismatch: {ident}')
    return len(catalog)

def manifest_paths(root=ROOT):
    root = Path(root)
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if not path.is_file() or any(part in {'.git', '__pycache__', '.venv', 'work', 'output', 'dist', '.pytest_cache'} for part in rel.parts):
            continue
        if rel.as_posix() == 'MANIFEST.sha256.json' or rel.name in {'params.json', 'params.local.json'}:
            continue
        if path.suffix in {'.pyc', '.pyo'}:
            continue
        yield rel.as_posix(), path

def build_manifest(root=ROOT):
    return {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in manifest_paths(root)}

def verify_manifest(root=ROOT):
    root = Path(root)
    expected = read_json(root / 'MANIFEST.sha256.json')
    actual = build_manifest(root)
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    changed = sorted(k for k in set(expected) & set(actual) if expected[k] != actual[k])
    if missing or extra or changed:
        raise ValidationError(f'Manifest mismatch: missing={missing}, added={extra}, changed={changed}')
    return len(expected)
