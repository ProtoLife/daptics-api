#!/bin/bash

# Start API_SERVER before running script
API_SERVER=${1:-http://localhost:4040}
status_code=`curl --write-out '%{http_code}' --silent --output /dev/null ${API_SERVER}/api?query=%7B__schema%7B%7D%7D`
if [[ "${status_code}" -ne 200 ]] ; then
  echo "Bad response from ${API_SERVER}: ${status_code}"
  exit 1
fi

GRAPHQL_MARKDOWN=`which graphql-markdown`
PDOC=`which pdoc`
MKDOCS=`which mkdocs`
cd -P -- "$(dirname -- "$0")"

cd pydocmd
${GRAPHQL_MARKDOWN} --no-toc --title 'Daptics GraphQL API' ${API_SERVER}/api >graphql_api.md
rc=$?
if [ "$rc" -ne 0 ]; then
    echo "----- graphql-markdown error"
    exit 1
fi
echo "----- graphql-markdown built successfully"

cd ../python_client
$PDOC --pdf --force --template-dir ../pdoc/templates daptics_client >../pydocmd/daptics_client.md
rc=$?
if [ "$rc" -ne 0 ]; then
    echo "----- pdoc error"
    exit 1
fi
echo "----- pdoc built successfully"

cd ..
$MKDOCS build
rc=$?
if [ "$rc" -ne 0 ]; then
    echo "----- mkdocs error"
    exit 1
fi
echo "----- mkdocs built successfully"
