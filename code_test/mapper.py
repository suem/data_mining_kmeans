#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np

from sklearn.cluster import KMeans

#D = 500
#k = 100


D = 500
k = 10

from sklearn.cluster import _k_means

def update_centers(X, labels, n_clusters, distances):
    print("X "),
    print(X)
    print("labels "),
    print(labels)
    print("n_clusters "),
    print(n_clusters)
    print("distances "),
    print(distances)
    
_k_means._centers_dense = update_centers
_k_means._centers_sparse = update_centers





def print_center(c):
    print("1\t"),
    for c_i in np.nditer(c):
        print(c_i),
    print('')


def print_centers(C):
    for i in range(C.shape[0]):
        print_center(C[i, :])


if __name__ == '__main__':

    features = []

    for line in sys.stdin:
        line = line.strip()
        features.append(np.fromstring(line, sep=' '))
    features = np.array(features).reshape((-1, D))

    kmeans = KMeans(n_clusters=k, precompute_distances=True)
    kmeans.fit(features)

    print_centers(kmeans.cluster_centers_)
