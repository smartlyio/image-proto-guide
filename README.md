# image-proto-guide

Guide to prototyping on top of vision APIs. Please read this file first.

# Requirements

1. Jupyter notebook, Python 3.6+, Pandas. You can get all of this at https://www.anaconda.com/download/#macos
2. Clone or download the repository
   - with git: `git clone git@github.com:smartlyio/image-proto-guide.git`
   - without git: https://github.com/smartlyio/image-proto-guide/archive/master.zip
3. Account to EyeEm Vision API to get clientId and app secret. Create account here: https://eyeem.3scale.net/
4. Download the dataset and extract into the repository. This creates a folder called data

# Overview

This exercise covers a simple end-to-end prototype for automatically selecting a the best pictures from a large set.
The prototype has the following steps.

- Using a ready-trained vision API to score images
- Building a model for selecting the scores
- Selecting pictures with the model

Start with the notebook: `source/Using vision APIs`

# Helpful Links

Introduction to Pandas:
https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb

Pandas documentation:
http://pandas.pydata.org/pandas-docs/stable/basics.html

## Disclaimer

Code examples are in python3, but feel free to fix code if you wish to use python 2.7
