#!/usr/bin/env bash

set -e

# build packages
. $(cd $(dirname $0); pwd)/artifacts.sh

ls -la $share_folder/build

ALL_MODULES=`find $share_folder/build/ -name "*.whl"`

# title 'Install azdev'
pip install -qqq -e ./tools
[ -d privates ] && pip install -qqq privates/*.whl
pip install -qqq $ALL_MODULES

azdev cli-lint
