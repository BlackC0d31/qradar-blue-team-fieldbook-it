.PHONY: check docs manifest
check:
	python3 verify_package.py
	python3 -m unittest discover -s tests -v
docs:
	python3 tools/build_docs.py
manifest:
	python3 tools/release.py --refresh-manifest
