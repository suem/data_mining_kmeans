#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np

#parallelization wouod be done best parallelizing distance computation, which is infeasible with map reduce
#instead, have a set of starting points for every mapper
for line in sys.stdin:
	line = line.strip()
	
	#TODO: create smart/random starting centers
	
	
	#run k-means
	
	
	#return clustering + maybe goodness of result
	#goodness = 1/N* sum( (x[i]-c[i])^2) #from pdf
	# print n_centers, centers, goodness
    
