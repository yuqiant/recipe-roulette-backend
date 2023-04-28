#!/bin/zsh

echo "Build starting"

pip install -r requirements.txt --target ./package
cd package || exit 1
zip -r ../dist.zip .
cd ../src || exit 1
zip -r ../dist.zip .