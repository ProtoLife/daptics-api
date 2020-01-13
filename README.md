# daptics API <a class="tocSkip"></a>

This is the README documentation for the daptics design of experiments GraphQL API
and the Python API client.


## Links

* The Python API client module and several tutorial Jupyter notebooks are available
from the daptics-api GitHub repository at
[https://github.com/ProtoLife/daptics-api](https://github.com/ProtoLife/daptics-api)
* Auto-generated documentation for the API and the client is available from the
GitHub Pages for this project at
[https://ProtoLife.github.io/daptics-api](https://ProtoLife.github.io/daptics-api)
* For more information on Daptics technology, please see the Documentation section
of the daptics website at [https://daptics.ai](https://daptics.ai)

To use the daptics API, you must first register at the [https://daptics.ai](https://daptics.ai)
to establish your login and password for API authentication.


## Python Client <a class="tocSkip"></a>

The `python_client` folder contains the Python GraphQL client, daptics_client.py,
and several interactive Python notebooks for experimenting with the API.

Follow the instructions in the README.md file in that folder to set up a local Jupyter Notebook
server if you do not have access to a server that can open `.ipynb` files.


## GraphQL API Documentation <a class="tocSkip"></a>

1. Install [graphql-markdown](https://www.npmjs.com/package/graphql-markdown)

2. Then in the `pydocmd` folder, run:

```
graphql-markdown http://inertia.protolife.com:8080/api >graphql_api.md
```

## Python Client Documentation and MkDocs Build <a class="tocSkip"></a>

1. Install these tools: [MkDocs](https://www.mkdocs.org/),
  the [ReadTheDocs-Dropdown theme for MkDocs](https://github.com/cjsheets/mkdocs-rtd-dropdown),
  and [pdoc3](https://pdoc3.github.io/pdoc/)

2. In the `python_client` folder, run: `pdoc --pdf --force --template-dir ../pdoc/templates daptics_client >../pydocmd/daptics_client.md`

3. Finally in the main project folder, run: `mkdocs build`


Html and Markdown files will be produced in the `docs` folder.


## Using Jupytext to Extract and Sync to Python Source Files <a class="tocSkip"></a>

1. Install [jupytext](https://github.com/mwouts/jupytext)

2. Set up metadata in any ipynb file that has Python code:
`jupytext --set-formats ipynb,python//py:light 03_SimpleTutorial.ipynb`

3. Export Python code to `/python` subdirectory:
`jupytext --from ipynb --to python//py:light 03_SimpleTutorial.ipynb`

4. Edit Python code as needed. Or when you run in Jupyter notebook, and make changes, the
corresponding Python file will be kept up to date!

5. Rebuild notebook from Python file without outputs (do this before checking into
version control):
`jupytext --from python//py:light --to notebook python/03_SimpleTutorial.py`

[![Automated Release Notes by gren](https://img.shields.io/badge/%F0%9F%A4%96-release%20notes-00B2EE.svg)](https://github-tools.github.io/github-release-notes/)
