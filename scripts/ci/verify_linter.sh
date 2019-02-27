#!/usr/bin/env bash

set -ev

. $(cd $(dirname $0); pwd)/artifacts.sh

ls -la $share_folder/build

ALL_MODULES=`find $share_folder/build/ -name "*.whl"`
echo $ALL_MODULES
pip install -e ./tools
[ -d privates ] && pip install -qqq privates/*.whl
pip install $ALL_MODULES

az ad user create -h
az -v
pip list

azdev cli-lint --ci
