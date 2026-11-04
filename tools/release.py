#!/usr/bin/env python3
"""Refresh the release manifest only after an explicit review decision."""
from pathlib import Path
import argparse,json,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from fieldbook import build_manifest,validate_catalog
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--refresh-manifest',action='store_true')
a=p.parse_args()
if not a.refresh_manifest:p.error('Use --refresh-manifest after reviewing intended changes')
validate_catalog()
(ROOT/'MANIFEST.sha256.json').write_text(json.dumps(build_manifest(),indent=2)+'\n',encoding='utf-8',newline='\n')
print('Release manifest refreshed; run verify_package.py and tests next.')
