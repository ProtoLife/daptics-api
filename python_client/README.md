# daptics_client - Python Client Package for the daptics API 

`daptics_client` encapsulates the GraphQL daptics API, a powerful
system for optimizing the design of experiments. Using `daptics_client`
you can integrate the daptics iterative optimizations into 
lab automation processes.

daptics allows you to specify complex experimental design spaces,
consisting of many numerical or categorical parameters, and uses
highly-tuned machine learning algorithms to produce sequential
batches of experimental designs (called "generations"), 
in an iterative process. 

After performing the designed experiments in a batch 
and scoring the assay results of each experiment in the batch
as a numeric response value, you upload these response values
via the API to produce the next generation of designs.

As the process continues, daptics explores the experimental
space to find potential optimal experiments for the next
batch.

For a detailed look at the underlying mathematics, 
see this white paper: https://daptics.ai/pdf/White.pdf

## Installation

Use `setuptools` to install the API modules on your Python system.

```sh
python3 setup.py install
```

Installation via `pip` coming soon!

## Examples - Jupyter Notebooks

Example tutorial Jupyter notebooks and more information are available from the 
repository website at https://github.com/ProtoLife/daptics-api

## Python Client and GraphQL API Reference Documentation

Documentation for both the client package and the low-level
GraphQL API can be found at https://protolife.github.io/daptics-api

## Web Access to the daptics System

A web interface to the system, together with more documentation and online help,
is available at https://daptics.ai
