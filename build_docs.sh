#!/bin/bash

API_SERVER=http://localhost:4040
BINDIR=/usr/local/bin

cd -P -- "$(dirname -- "$0")"
cd pydocmd
$BINDIR/graphql-markdown --no-toc --title 'Daptics GraphQL API' ${API_SERVER}/api >graphql_api.md
cd ../python_client
$BINDIR/pdoc --pdf --force --template-dir ../pdoc/templates daptics_client >../pydocmd/daptics_client.md
cd ..
$BINDIR/mkdocs build
