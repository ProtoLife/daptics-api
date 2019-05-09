# daptics-api

Documentation and clients for the Daptics design of experiments GraphQL API.

For more information on Daptics technology, please see the Documentation section
of the [Daptics website](https://daptics.ai).

To use the Daptics API, you must first register at the [Daptics website](https://daptics.ai)
to establish your login and password for API authentication.


## Python Client

The `python_client` folder contains the Python GraphQL client, daptics_client.py,
and several interactive Python notebooks for experimenting with the API.

Follow the instructions in the README.md file to set up a local Jupyter Notebook
server if you do not have access to a server that can open `.ipynb` files.


[![Automated Release Notes by gren](https://img.shields.io/badge/%F0%9F%A4%96-release%20notes-00B2EE.svg)](https://github-tools.github.io/github-release-notes/)


## GraphQL API Documentation

Install this tool:

* [graphql-markdown]()

Then in `docs` folder, run:

```
graphql-markdown http://inertia.protolife.com:8080/api >graphql_api.md
```

## Python Client Documentation and MkDocs Build

Install these tools:

* [MkDocs](https://www.mkdocs.org/)
* [pydocmd](https://niklasrosenstein.github.io/pydoc-markdown)

Then in `docs` folder, run:

```
pydocmd build
```

Html and Markdown files will be produced in the `docs/_build/site` folder.


## Using jupytext to extract and sync to Python source files

1. Install jupytext:

* [jupytext](https://github.com/mwouts/jupytext)

2. Set up metadata in any ipynb file that has Python code:

```
jupytext --set-formats ipynb,python//py:light 03_SimpleTutorial.ipynb
```

3. Export Python code to `/python` subdirectory:

```
jupytext --from ipynb --to python//py:light 03_SimpleTutorial.ipynb
```

4. Edit Python code as needed. Or when you run in Jupyter notebook, and make changes, the
corresponding Python file will be kept up to date!

5. Rebuild notebook from Python file without outputs (do this before checking into
version control):

```
jupytext --from python//py:light --to notebook python/03_SimpleTutorial.py
```
