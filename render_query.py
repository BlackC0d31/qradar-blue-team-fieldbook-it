#!/usr/bin/env python3
"""Render/list/show query templates locally; never execute AQL."""
import argparse
import json
import sys
from fieldbook import ROOT, ValidationError, load_catalog, read_json, render, write_output

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('id', nargs='?', help='Q001-Q110 or OPT01-OPT07')
    parser.add_argument('--list', action='store_true', help='List IDs and titles')
    parser.add_argument('--show', action='store_true', help='Show metadata for the selected ID')
    parser.add_argument('--params', help='UTF-8 JSON parameter file')
    parser.add_argument('--output', help='Write UTF-8 AQL instead of stdout')
    parser.add_argument('--force', action='store_true', help='Replace an existing --output file')
    args = parser.parse_args(argv)
    try:
        catalog = load_catalog()
        if args.list:
            for ident, item in catalog.items():
                print(ident + '  ' + item['title'])
            return 0
        if not args.id:
            parser.error('a query ID or --list is required')
        if args.id not in catalog:
            raise ValidationError('Unknown query ID: ' + args.id)
        if args.show:
            print(json.dumps(catalog[args.id], ensure_ascii=False, indent=2))
            return 0
        if not args.params:
            parser.error('--params is required when rendering')
        if args.force and not args.output:
            parser.error('--force requires --output')
        sql = render(args.id, read_json(args.params))
        if args.output:
            write_output(args.output, sql, force=args.force)
        else:
            # Explicit UTF-8 is also available through python -X utf8 on Windows.
            print(sql, end='')
        return 0
    except (ValidationError, OSError) as exc:
        print('ERROR: ' + str(exc), file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
