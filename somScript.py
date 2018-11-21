
import numpy as np
import pandas as pd
train = pd.read_csv('train.csv')

import matplotlib.pyplot as plt


import seaborn as sns
import SimpSOM as sps

train_sample = train.sample(5000)
target = train_sample['label']
train_sample = train_sample.drop(labels = ['label'],axis = 1)

sns.countplot(target)

train_input = train_sample.values
net = sps.somNet(20,20,train_input,PBC = True)
plt.imshow(np.asarray(net.nodeList[100].weights).reshape(28,28))

net.train(0.1,1000)

test = train.sample(10000)
test_targets = test['label']
test_input = test.drop(labels = 'label',axis = 1 ).values

projData = net.project