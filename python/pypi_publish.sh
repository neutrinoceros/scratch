#!/usr/bin/env bash

set -euxo pipefail

### 0) clean dir
rm -fr dist build

### 1) install tools
python -m pip install --upgrade twine wheel

### 2) build wheel
# old way
#python setup.py sdist bdist_wheel
# modern alternative
python -m build

### 3) deploy
# for a test publication
#twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# for an actual publication
#twine upload dist/*
