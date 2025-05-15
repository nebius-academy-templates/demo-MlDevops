from sklearn.cluster import  DBSCAN
import numpy as np

#Simulate metrics
metrics = np.array([[0.1,0.2], [0.2, 0.3], [0.25, 0.5], [6.0, 0.8], [0.1,0.2], [0.2, 0.3], [7.25, 5.5], [1.0, 0.8]])


#DBSCAN clustering

dbs = DBSCAN(
    eps=0.5,min_samples=2
).fit(metrics)

print(metrics[dbs.labels_ == -1])