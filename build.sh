#!/bin/bash

echo "Install dependencies"
python -m pip install --upgrade pip
pip install -r requirements.txt --target ./package

echo "Running Test"
python -m unittest discover -s ./test || exit 1

echo "Pre-build clean up cache"
rm dist.zip
find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

echo "Build starting"
cd package || exit 1
zip -r ../dist.zip .
cd ../src || exit 1
zip -r ../dist.zip .

echo "Post-build clean up"
cd .. || exit 1
rm -rf package