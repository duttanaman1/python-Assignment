#  analysis of linear systems involving Vandermonde matrix
from LUPsolve import LUPsolve
from VanderBuild import VanderBuild
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lu

xax = np.array([])
yax = np.array([])
for N in range(15,26):

    V = VanderBuild(N)

    c= np.zeros(N+1)

    for i in range(N+1):
        c[i] = V[i,N]

    X_exact, L, U, P = LUPsolve(V,c)

    x = lu.solve(V,c)

    calc = ((X_exact-x)/x)*100

    xax = np.append(xax, X_exact)
    yax = np.append(yax,calc)

plt.plot(xax, yax)
plt.show()
  


   
   # compute the error
   
   # compute the max relative error 


# plot error and max relative error versus the matrix size on a logarithmic scale on the y-axis (semilogy) 






