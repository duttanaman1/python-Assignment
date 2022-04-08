#  solves Ax=b by via the decomposition PA = LU

import numpy as np
import scipy.linalg as lu

def LUPsolve(A,b):  # inputs n x n numpy array A, and n x 1 numpy array b
    
    P, L, U = lu.lu(A)
    lx, piv = lu.lu_factor(A)
    x = lu.lu_solve((lx, piv),b)
        
    return x, L, U, P  # outputs solution x, and numpy arrays L, U and P from PA = LU decomposition






