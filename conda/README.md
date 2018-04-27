# Deep Learning  - Conda Environment

Creates a Conda environemt for Deep Learning with Tensorflow, Keras, Pandas, SciPy, SKLearn, Pandas, Seaborn

## Refer
https://conda.io/docs/user-guide/tasks/manage-environments.html

## To create an environment
conda env create -f dl_env.yml

# Test if everything is up & running 

(Adapted from: https://github.com/leriomaggio/deep-learning-keras-tensorflow)

## 1. Check import


```python
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
```


```python
import keras
```

    Using TensorFlow backend.


## 2. Check installed Versions


```python
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
```

    numpy: 1.11.1
    scipy: 0.18.0
    matplotlib: 1.5.2
    iPython: 5.1.0
    scikit-learn: 0.18



```python
import keras
print('keras: ', keras.__version__)

# optional
import theano
print('Theano: ', theano.__version__)

import tensorflow as tf
print('Tensorflow: ', tf.__version__)
```

    keras:  2.0.2
    Theano:  0.9.0
    Tensorflow:  1.0.1
