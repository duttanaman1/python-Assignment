#  analysis of matrix-vector products with 
#    tridiagonal matrix A

import numpy as np
import time                     # for timing the banded_matvec function
import matplotlib.pyplot as plt
from Tridiag_Matvec import Tridiag_Matvec   # your banded_matvec function

# loop over matrix sizes
xax = np.array([])
yax = np.array([])
for k in range(8):

   n = np.power(10,k)
   
   # generate random arrays a, b, c and x using numpy.random.rand or fix them, for instance to all 1s.

   a= np.random.rand(n)
   b= np.random.rand(n)
   c= np.random.rand(n)
   x = np.random.rand(n)


   # start the timer

   start = time.time()

   # call Tridiag_Matvec
   Tridiag_Matvec(a,b,c,x)

   # stop the timer and store the wall time
   stop = time.time()
   xax = np.append(xax,n)
   yax = np.append(yax,stop-start)

   

# plot the wall time versus the matrix size on a logarithmic scale along with your prediction


plt.plot(xax, yax)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('wall time')
plt.xlabel('N value')
plt.show()