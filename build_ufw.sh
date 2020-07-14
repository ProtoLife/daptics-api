#!/bin/bash

# Run build_docs.sh script first!
# This script uses graphql-markdown and pdoc output from that script.
# Output is sent to destination specified in alternate configuration file.

MKDOCS=`which mkdocs`
cd -P -- "$(dirname -- "$0")"

$MKDOCS build -f ./user_front_web.yml
rc=$?
if [ "$rc" -ne 0 ]; then
    echo "----- mkdocs error"
    exit 1
fi
echo "----- mkdocs built successfully"
