#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np

from sklearn.cluster import KMeans

D = 500
k = 100


def print_center(c):
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
        key, feature = line.split('\t', 1)
        features.append(np.fromstring(feature, sep=' '))
    features = np.array(features).reshape((-1, D))

    kmeans = KMeans(n_clusters=k)
    kmeans.fit(features)

    print_centers(kmeans.cluster_centers_)
    
