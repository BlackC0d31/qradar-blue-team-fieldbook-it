"""Behavioral tests for the offline renderer and file-safety boundaries."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import fieldbook

class RendererTests(unittest.TestCase):
    def test_minimal_ip_query(self):
        sql = fieldbook.render('Q001', {'IP': '192.0.2.10'})
        self.assertEqual(sql.count("'192.0.2.10'"), 2)
        self.assertNotIn('<IP>', sql)

    def test_only_used_values_are_required(self):
        self.assertIn('SELECT', fieldbook.render('Q001', {'IP': '192.0.2.10', 'LS_FW': None}))

    def test_missing_and_unknown_identity(self):
        for ident, params in [('Q001', {}), ('Q999', {'IP': '192.0.2.10'})]:
            with self.assertRaises(fieldbook.ValidationError):
                fieldbook.render(ident, params)

    def test_invalid_ipv4_and_literal_injection(self):
        for ip in ['192.0.2.999', "192.0.2.10' OR 1=1", '::1', '<IP>', '192.0.2.10\n']:
            with self.assertRaises(fieldbook.ValidationError):
                fieldbook.render('Q001', {'IP': ip})

    def test_bool_is_not_an_id(self):
        with self.assertRaises(fieldbook.ValidationError):
            fieldbook.render('Q008', {'IP': '192.0.2.10', 'LS_FW': True})

    def test_date_order_and_calendar(self):
        base = {'IP': '192.0.2.10', 'START': '2026-11-04 09:00:00', 'STOP': '2026-11-04 09:05:00'}
        self.assertIn("STOP '2026-11-04 09:05:00'", fieldbook.render('Q015', base))
        for stop in ['2026-11-04 08:59:59', base['START'], '2026-02-30 10:00:00']:
            with self.assertRaises(fieldbook.ValidationError):
                fieldbook.render('Q015', dict(base, STOP=stop))

    def test_bom_and_duplicate_json_keys(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'params.json'
            path.write_text('\ufeff{"IP":"192.0.2.10"}', encoding='utf-8')
            self.assertEqual(fieldbook.read_json(path)['IP'], '192.0.2.10')
            path.write_text('{"IP":"192.0.2.10","IP":"192.0.2.11"}', encoding='utf-8')
            with self.assertRaises(fieldbook.ValidationError):
                fieldbook.read_json(path)

    def test_outputs_are_not_overwritten_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'nested' / 'query.aql'
            fieldbook.write_output(path, 'first\n')
            with self.assertRaises(fieldbook.ValidationError):
                fieldbook.write_output(path, 'second\n')
            self.assertEqual(path.read_text(encoding='utf-8'), 'first\n')
            fieldbook.write_output(path, 'second\n', force=True)
            self.assertEqual(path.read_text(encoding='utf-8'), 'second\n')

    def test_cli_failure_does_not_create_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            params = Path(tmp) / 'params.json'; output = Path(tmp) / 'result.aql'
            params.write_text('{}', encoding='utf-8')
            result = subprocess.run([sys.executable, str(fieldbook.ROOT/'render_query.py'), 'Q001', '--params', str(params), '--output', str(output)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())

    def test_all_templates_accept_schema_examples(self):
        schema = fieldbook.read_json(fieldbook.ROOT/'parameter_schema.json')
        params = {k: v['example'] for k, v in schema.items()}
        for ident in fieldbook.load_catalog():
            with self.subTest(query=ident):
                self.assertNotRegex(fieldbook.render(ident, params), r'<[A-Z_]+>')

    def test_catalog_and_release_integrity(self):
        self.assertEqual(fieldbook.validate_catalog(), 117)
        self.assertGreater(fieldbook.verify_manifest(), 117)

if __name__ == '__main__':
    unittest.main()
