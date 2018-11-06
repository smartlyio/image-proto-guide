# image-proto-guide

Guide to prototyping on top of vision APIs. Please read this file first.

# Requirements

1. Jupyter notebook, Python 3.6+, Pandas. You can get all of this at https://www.anaconda.com/download/#macos
2. Git client to clone this repository, or just download the repo as a zip.
3. Account to EyeEm Vision API to get clientId and app secret. Create account here: https://eyeem.3scale.net/

# Overview

This exercise covers a simple end-to-end prototype for automatically selecting a the best pictures from a large set.
The prototype has the following steps.

- Using a ready-trained vision API to score images
- Building a model for selecting the scores
- Selecting pictures with the model

Start with the notebook: `source/Using vision APIs`

## Disclaimer

Code examples are in python3, but feel free to fix code if you wish to use python 2.7
