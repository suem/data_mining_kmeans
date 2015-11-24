#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np

from sklearn.cluster import KMeans

D = 500
k = 100


def print_center(c):
    print('1\t'),
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

    kmeans = KMeans(n_clusters=k, precompute_distances=False)
    kmeans.fit(features)

    print_centers(kmeans.cluster_centers_)
