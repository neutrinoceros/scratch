#!/usr/bin/env bash

set -euxo pipefail

python3 -m pip install --upgrade twine wheel
rm -fr dist build
python3 setup.py sdist bdist_wheel

# for a test publication
#twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# for an actual publication
#twine upload dist/*
