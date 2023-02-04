#!/usr/bin/env bash
# copy this file to your project dir, make sure to review and set all constants
# ASSUMPTIONS:
# - metadata should live in pyproject.toml (only required if TEST=1 to test install)
# - this script should work with Python 3.7+

### user defined constants
TEST=1  # set to 0 to upload to the actual PyPI server (test.pypi is used otherwise)


### 0) clean dir
rm -fr dist build publish_venv

### 1) create env
python -m venv publish_venv
source publish_venv/bin/activate

set -euxo pipefail
python -m pip install --upgrade pip
python -m pip install --upgrade build
python -m pip install --upgrade twine


### 2) build wheel
python -m build


### 3) deploy
if [ $TEST ]; then
    INDEX_URL=https://test.pypi.org/legacy/
else
    INDEX_URL=https://pypi.org
fi

twine upload dist/* --repository-url $INDEX_URL


### 4) test install
if [ ! $TEST ]; then
    exit 0
fi

PY311=$(python -c "import sys; print(int(sys.version_info >= (3, 11)))")
if [ ! "$PY311" ]; then
    python -m pip install tomli
fi

PROJECT_NAME=$(python -c """
import sys
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

with open('pyproject.toml', 'rb') as fh:
    project_name = tomllib.load(fh)['project']['name']
print(project_name)
""")

python -m pip install "$PROJECT_NAME" \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple/
