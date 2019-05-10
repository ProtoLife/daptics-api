# DapticsClient Tutorials - README

This project is a Jupyter Python notebook that gives a brief interactive introduction
to using the daptics API with a freely distributed Python GraphQL client.

See the documentation at https://jupyter.org if you have never used Jupyter notebooks before.

For additional help or information, please visit or contact Daptics.

On the web at https://daptics.ai  
By email at support@daptics.ai

Daptics API Version 0.7.0  
Copyright (c) 2019 Daptics Inc.

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


### Installation

Before opening the Introduction notebook, install IPython, Jupyter and required packages.

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

https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter


### Tutorial Contents

The tutorials folder contains an introductory Jupyter notebook, Introduction.ipynb,
and supporting files.  Make sure to import all the files in this folder into your
Jupyter server, especially the daptics_client.py file that the notebook will import.

There are also several example experimental space definition CSV files in the
folder that you can use to try out different parameters.
