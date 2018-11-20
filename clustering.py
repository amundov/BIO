import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd
import seaborn as sns; sns.set()


clustering = DBSCAN(eps=1,min_samples = 2).fit(points)
labels = list(clustering.labels_)

colors = [plt.cm.Spectral(each) for each in np.linspace(0,1,len(set(labels)))]

df1 = pd.DataFrame(points, columns = ['x','y'])
df2 = pd.DataFrame(target,columns = ['target'])
df3 = pd.DataFrame(labels,columns = ['labels'])

df4 = pd.concat([df1,df2,df3] , axis =1,join = 'inner')

x,y,target,lab =df4['x'].values,df4['y'].values, df4['target'].values,df4['labels'].values

ax = sns.scatterplot(x,y,hue = target)



