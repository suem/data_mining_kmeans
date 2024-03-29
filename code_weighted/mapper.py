#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np

from sklearn.cluster import KMeans

D = 500
k = 500
k_final = 950.0


def print_center(c):
    print("1\t"),
    for c_i in np.nditer(c):
        print(c_i),
    print('')


def print_centers(C, weights):
    for i in range(C.shape[0]):
        # for j in range(int(k_final/weights[i])):
        c = max(int(weights[i]*k_final),1)
        for j in range(c):
            print_center(C[i, :])


if __name__ == '__main__':

    features = []

    for line in sys.stdin:
        line = line.strip()
        features.append(np.fromstring(line, sep=' '))
    features = np.array(features).reshape((-1, D))

    kmeans = KMeans(n_clusters=k, precompute_distances=True)
    kmeans.fit(features)
    weights = [0.0 for i in range(k)]
    for i in range(len(kmeans.labels_)):
        weights[kmeans.labels_[i]] += 1.0

    for i in range(k):
        weights[i] /= float(len(kmeans.labels_))

    print_centers(kmeans.cluster_centers_, weights)
