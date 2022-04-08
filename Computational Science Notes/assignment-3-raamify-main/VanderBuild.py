#  builds the Vandermonde matrix

import numpy as np


def VanderBuild(N):  # inputs integer N
    
    V = np.zeros((N+1,N+1))

    for i in range(N+1):
        V[i,0]=1
    
    for i in range(N+1):
        for j in range(1,N+1):
            V[i,j]= np.power((1/N)*i,j)
    
    return V   # outputs the N+1 x N+1 numpy array with Vandermonde matrix