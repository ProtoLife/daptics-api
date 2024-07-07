# daptics API <a class="tocSkip"></a>

This is the README documentation for the daptics Design of Experiments GraphQL API
and the Python API client.

## Links

* The Python API client package and several tutorial Jupyter notebooks are available
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

The `python_client` folder contains the Python GraphQL client package module 
sources (in the `daptics_client`, `phoenix`, and `syncasync` folders),
and several interactive Python notebooks for experimenting with the API.

Follow the instructions in the README-NOTEBOOKS.md file in that folder to set up a local Jupyter Notebook
server if you do not have access to a server that can open `.ipynb` files.

## GraphQL API Documentation <a class="tocSkip"></a>

1. Install [graphql-markdown](https://www.npmjs.com/package/graphql-markdown)

2. Then in the `pydocmd` folder, run:

```
NODE_TLS_REJECT_UNAUTHORIZED=0 graphql-markdown --no-toc --title 'Daptics GraphQL API' https://api.daptics.ai/api >graphql_api.md
```

Notes: 

1. The `NODE_TLS_REJECT_UNAUTHORIZED=0` is to handle our ZeroSSL certificates.

2. If this fails, you can use the appropriate JSON schema file to generate
the docs, with this command:

```
graphql-markdown --no-toc --title 'Daptics GraphQL API' api-0.14.1.json >graphql_api.md
```

2. If using `yarn` to manage node packages, try this:

```
yarn bin graphql-markdown
```

to get the location of the `graphql-markdown` executable.


## Python Client Documentation and MkDocs Build <a class="tocSkip"></a>

1. Install these tools in order: 

    a. [tornado](https://www.tornadoweb.org/) - Important! Specify version 5.1.1 (version 6.0 will break MkDocs)
    b. [pdoc3](https://pdoc3.github.io/pdoc/) 
    c. [MkDocs](https://www.mkdocs.org/)
    d. [mkdocs-rtd-dropdown](https://github.com/cjsheets/mkdocs-rtd-dropdown) - Theme for MkDocs

2. Create Markdown documentation for the `daptics_client.py` file using `pdoc3`. In the
`python_client` folder, run:
`pdoc3 --pdf --force --template-dir ../pdoc/templates daptics_client >../pydocmd/daptics_client.md`

3. Then build the entire "Read the Docs" site, using `mkdocs`. In the root project folder,
where the `mkdocs.yml` configuration file is located, run: `mkdocs build`

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

You can also use `jupyter nbconvert` to remove all output from .ipynb files:

```
jupyter nbconvert 03_SimpleTutorial.ipynb --to notebook --ClearOutputPreprocessor.enabled=True --inplace
```

[![Automated Release Notes by gren](https://img.shields.io/badge/%F0%9F%A4%96-release%20notes-00B2EE.svg)](https://github-tools.github.io/github-release-notes/)
