# Jupyter Notebooks

This folder of Python Jupyter notebooks gives a brief interactive introduction
to using the daptics API with a freely distributed Python API client.

See the documentation at [https://jupyter.org](https://jupyter.org) if you have never used
Jupyter notebooks before.

Please note that to use the daptics API, you must first have a daptics account.
To create an account, or to get help or information on daptics, please visit or contact us:

* On the web at <a href="https://daptics.ai">https://daptics.ai    
* By email at [support@daptics.ai](mailto:support@daptics.ai)


## Installation

Before opening the `01_README.ipynb` notebook, install IPython, Jupyter and required packages.

a) with conda:

```
conda install -c conda-forge requests gql ipython jupyter
```

or b) with pip:

```
# first, always upgrade pip!
pip install --upgrade pip
pip install --upgrade requests gql ipython jupyter
```

Start the notebook in the tutorial directory:

```
cd tutorials
jupyter notebook
```

Then open the Introduction.ipynb notebook. If running the cells in the notebook have
problems with library imports, see this article for how you might have to import the
correct versions of the required `requests` and `gql` libraries:

[https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter)


## Tutorial Notebooks

This folder contains a series of Jupyter notebooks to explain operation of the daptics API, with explicit examples:

* 01_README.ipynb
* 02_Terminology.ipynb
* 03_SimpleTutorial.ipynb
* 04_GetAnalytics.ipynb
* 05_RestartSession.ipynb
* 06_AutomationWorkflow.ipynb

If you are familiar with daptics from the web interface, you could jump directly to `03_SimpleTutorial.ipynb` to get started.

Make sure to copy all the files in this folder into your
Jupyter server directory (the directory from which you start `jupyter notebook`), especially the three package folders that the all notebooks using the daptics API  will import:

* `daptics_client`
* `phoenix`
* `syncasync`

There are also several example experimental space definition CSV files in this
folder that you can use to try out different parameters.

```python
# Here's an example of using conda to update the required libraries in Jupyter-land.

import sys
print(sys.path)
print('Using {} to run pip'.format(sys.executable))
!{sys.executable} -m pip install requests gql async_timeout websockets
```

## Copyright Notice

Daptics API Version 0.15.1  
Copyright (c) 2024 Daptics Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), the rights to use, copy, modify, merge,
publish, and/or distribute, copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

You do not have the right to sub-license or sell copies of the Software.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
