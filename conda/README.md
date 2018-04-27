# Deep Learning  - Conda Environment

Creates a Conda environemt for Deep Learning with Tensorflow, Keras, Pandas, SciPy, SKLearn, Pandas, Seaborn

## Refer
https://conda.io/docs/user-guide/tasks/manage-environments.html

## To create an environment
conda env create -f dl_env.yml

## Test if everything is up & running
1. Check import
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import keras
Using TensorFlow backend.
2. Check installed Versions
import numpy
print('numpy:', numpy.__version__)

import scipy
print('scipy:', scipy.__version__)

import matplotlib
print('matplotlib:', matplotlib.__version__)

import IPython
print('iPython:', IPython.__version__)

import sklearn
print('scikit-learn:', sklearn.__version__)
numpy: 1.11.1
scipy: 0.18.0
matplotlib: 1.5.2
iPython: 5.1.0
scikit-learn: 0.18
import keras
print('keras: ', keras.__version__)

# optional
import theano
print('Theano: ', theano.__version__)

import tensorflow as tf
print('Tensorflow: ', tf.__version__)
keras:  2.0.2
Theano:  0.9.0
Tensorflow:  1.0.1
