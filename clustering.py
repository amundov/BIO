from sklearn import cluster
from scipy import stats


clustering = DBSCAN(eps=0.2,min_samples = 1).fit(projData[:])
#clustering = sklearn.cluster.SpectralClustering(n_clusters =190, eigen_solver = 'arpack',affinity = 'nearest_neighbors').fit(projData)
labels = list(clustering.labels_)

#colors = [plt.cm.Spectral(each) for each in np.linspace(0,1,len(set(labels)))]
target = test_targets.values

predicted_labels = clustering.fit_predict(testProj)

df1 = pd.DataFrame(testProj, columns = ['x','y'])
df2 = pd.DataFrame(target[:1000],columns = ['target'])
df3 = pd.DataFrame(predicted_labels,columns = ['labels'])

df4 = pd.concat([df1,df2,df3] , axis =1,join = 'inner')

x,y,target,lab =df4['x'].values,df4['y'].values, df4['target'].values,df4['labels'].values

ax = sns.scatterplot(x,y,hue = lab)

for i in set(df4['labels'].values):
    print(df4[df4['labels'] == i ])
    
def evaluate(df):
    total_corr =0
    total_num = 0
    targets = list(set(df['target']))
    target_counts = np.zeros(np.shape(targets))
    for i in set(df['labels'].values):
        modearr = stats.mode(df[df['labels']==i]['target'].values)
        mode,count = modearr[0][0],modearr[1][0]
        num = len(df[df['labels']==i]['target'])
        
        total_num+=num
        total_corr+=count
    return(total_corr/total_num)
    
    