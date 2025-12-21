#!/usr/bin/env bash
set -o errexit
set -o nounset

cd ../
. ./.venv/bin/activate
cd examples/

mkdir -p reports
python3 _pandasreporter.py