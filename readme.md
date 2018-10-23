# TdaToolbox 

Please give credit to Coricos(https://github.com/Coricos), which is the person I forked it from. This specific package is more less the same as the one on Coricos, but with a more straightforward installation, i.e. it just requires conda more os less. 

## Instructions

1. Install miniconda or any conda distribution
2. After installation, create a virtualenv using conda, stick to python3.6. Preferably use: conda create --name myenv python=3.6
3. run the line conda install -c conda-forge gudhi 
4. run pip install -r requirements.txt
5. Start TDA:ing!

## Introduction

Topological Data Analysis, also abbreviated *TDA*, is a recent field that emerged from various works in applied topology and computational geometry. It aims at providing well-founded mathematical, statistical and algorithmic methods to exploit the topological and underlying geometric structures in data. My aim is to develop some tools in this repository, that may be applied to data science in general. Some of them already proved useful for classification tasks.

## 3DShape

This _notebook_ gives a simple example of how to handle three-dimensional shapes. The whole example is based on the height as filtration function, so not invariant in space. However, it gives a pretty good idea of what the output of a topological analysis may give.

## ToMaTo Clustering

This _notebook_ rather focus on a specific strength of TDA: its robustness to detect centroids in dataset, along with its ability to record the relationships between each point, enabling us to retrace the whole structure of the centroids. Examples are provided in the notebook.

## TimeSeries

This _section_ is still in construction.
