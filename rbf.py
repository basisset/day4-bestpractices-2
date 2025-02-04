from math import exp
import numpy as np
from scipy.interpolate import Rbf

# Naive python implementation of a Radial Basis Function (RBF) approximation scheme
#@profile ### time = 10s
def rbf_network(X, beta, theta):

    N = X.shape[0]
    D = X.shape[1]
    Y = np.zeros(N)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):               ### Loop in a loop slows things down
                r += (X[j, d] - X[i, d]) ** 2### Elementwise subtraction takes a long time 
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y

# Scipy implementation of a Radial Basis Function (RBF) approximation scheme
#@profile ### time = 0.053 s, 200 times faster
def rbf_scipy(X, beta):

    N = X.shape[0]
    D = X.shape[1]    
    rbf = Rbf(X[:,0], X[:,1], X[:,2], X[:,3], X[:, 4], beta) ### Scipy already has this implemented
    #Xtuple = tuple([X[:, i] for i in range(D)])
    Xtuple = tuple([X[:, i] for i in range(D)])

    return rbf(*Xtuple)


# Cython  implementation of a Radial Basis Function (RBF) approximation scheme
# 
# TODO: Write the Cython implementation in a separate fastloop.pyx file, compile and import it here
# 
from fastloop import rbf_network_cython


# Make up some data
D = 5
N = 1000
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10

# Simple testing of the performance of the Python and Scipy implementations
#@profile
import time


#rbf_network(X, beta, theta)

#rbf_scipy(X, beta)

t0 = time.time()
rbf_network(X, beta, theta)
print("Python: ", time.time() - t0)

t0 = time.time()
rbf_scipy(X, beta)
print("Scipy: ", time.time() - t0)

# Testing the performance of Cython
### time = 0.055 s, fasten than Python bit still slower than cython
t0 = time.time()
rbf_network_cython(X, beta, theta)
print("Cython: ", time.time() - t0)











        
