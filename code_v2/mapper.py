#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np

from sklearn.cluster import KMeans

D = 500
k = 200


def get_cluster_sizes(labels):
    cluster_sizes = []
    for i in range(k):
        cluster_sizes.append(np.sum(labels == i))
    return cluster_sizes


def print_center(cluster_size, c):
    print('%s\t' % cluster_size),
    for c_i in np.nditer(c):
        print(c_i),
    print('')


def print_centers(cluster_sizes, C):
    for i in range(C.shape[0]):
        print_center(cluster_sizes[i], C[i, :])


if __name__ == '__main__':

    features = []

    for line in sys.stdin:
        line = line.strip()
        features.append(np.fromstring(line, sep=' '))
    features = np.array(features).reshape((-1, D))

    kmeans = KMeans(n_clusters=k, precompute_distances=True, n_init=30)
    kmeans.fit(features)

    cluster_sizes = get_cluster_sizes(kmeans.labels_)
    print_centers(cluster_sizes, kmeans.cluster_centers_)
