#!/usr/bin/env python3
"""Verify release integrity and catalog/file consistency, not Ariel parsing."""
import sys
from fieldbook import ValidationError, validate_catalog, verify_manifest

def main():
    try:
        queries = validate_catalog()
        files = verify_manifest()
    except (ValidationError, OSError) as exc:
        print('ERROR: ' + str(exc), file=sys.stderr)
        return 1
    print(f'OK: {queries} query templates; {files} files match the release manifest.')
    print('Offline structural checks only. Ariel parsing/execution is NOT verified.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
