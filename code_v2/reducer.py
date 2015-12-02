#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np

from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.preprocessing import normalize

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

    cluster_sizes = []
    centers = []

    for line in sys.stdin:
        #read "coresets" = (cluster_sizes[i], C[i, :])
        line = line.strip()
        cluster_size, center = line.split('\t', 1)
        cluster_sizes.append(int(cluster_size))
        centers.append(np.fromstring(center, sep=' '))
    cluster_sizes = np.array(cluster_sizes)
    centers = np.array(centers).reshape((-1, D))

    n_clusters = len(cluster_sizes)
    #merge random "coresset" (=row) with closest, until n_clusters == k    
    while n_clusters > k:
        #random i
        i = np.random.randint(n_clusters)
        c = centers[i, :]
        #remove cluster i        
        centers = np.delete(centers, (i), axis=0)
        size = cluster_sizes[i]
        cluster_sizes = np.delete(cluster_sizes, (i))
        #find closest distance d at pos j
        d = pairwise_distances(centers)
        j = np.argmin(d)
        #merge i and j
        centers[j, :] = ((cluster_sizes[j]*centers[j, :] + size*c)/
                         (cluster_sizes[j] + size))
        cluster_sizes[j] += size
        n_clusters -= 1

    print_centers(centers)
