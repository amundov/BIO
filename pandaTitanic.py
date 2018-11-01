# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:44:37 2018

@author: amundov
"""

import sys 

import pandas as pd
import matplotlib
import numpy as np
import scipy as sp
import IPython
from IPython import display
import sklearn

import random
import time

import warnings
warnings.filterwarnings('ignore')
print('_'*25)

import os
os.listdir('C://Users//amundov//Documents//Python Scripts//Titanic')

from sklearn import svm, tree, linear_model, neighbors, naive_bayes, ensemble, discriminant_analysis, gaussian_process


from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn import feature_selection
from sklearn import model_selection
from sklearn import metrics

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns
from pandas.tools.plotting import scatter_matrix

%matplotlib inline
mpl.style.use('ggplot')
sns.set_style('white')
pylab.rcParams['figure.figsize'] = 12,8

data_raw = pd.read_csv('C://Users//amundov//Documents//Python Scripts//Titanic/train.csv')
data_val = pd.read_csv('C://Users//amundov//Documents//Python Scripts//Titanic/test.csv')
