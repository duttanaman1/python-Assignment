# function for computing the matrix vector product 
#    where A is a tridiagonal matrix
import numpy as np

def Tridiag_Matvec(a,b,c,x):
    # Insert code to compute the product y of the tridiagonal matrix A (specified by a, b and c) with vector x.
    n = len(x)
    y = np.zeros(n)

    for i in range(0,n-2):
        y[i] = a[i]*x[i] + b[i]*x[i+1] + c[i]*x[i+2]
    
    y[n-2] = a[n-2]*x[n-2] + b[n-2]*x[n-1]

    y[n-1] = a[n-1]*x[n-1]

    return y   # y = Ax
