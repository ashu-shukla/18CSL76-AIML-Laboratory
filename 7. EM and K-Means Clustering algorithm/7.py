import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans


# Importing the dataset
data = pd.read_csv('ex.csv')
print("Input Data and Shape")
print(data)


# Getting the values and plotting it
f1 = data['V1'].values
f2 = data['V2'].values


# Create a new data array/matrix with f1 and f2
X = np.array(list(zip(f1, f2)))


# Scatter plot of the matrix
print('Graph for whole dataset')
plt.scatter(f1, f2, c='black')
plt.show()

# KMeans Clustering
kmeans = KMeans(2, random_state=0)

labels = kmeans.fit(X).predict(X)
centroids = kmeans.cluster_centers_


plt.scatter(X[:, 0], X[:, 1], c=labels, s=40)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='g')
plt.show()


# Gaussian Mixture
print('Graph using EM Algorithm')
gmm = GaussianMixture(n_components=2).fit(X)
labels = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50)
plt.show()
