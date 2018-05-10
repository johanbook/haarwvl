# -*- coding: utf-8 -*-
"""
Created on Mon May  7 13:34:28 2018

@author: Frank Johansson
"""

import numpy as np
from scipy import *

def transform(matrix, weight = sqrt(2)):
    W, Winverse = wavelet(matrix, weight, orthagonal = (weight == sqrt(2)))
    return W * matrix * Winverse

def inverse_transform(matrix, weight = sqrt(2)):
    W, Winverse = wavelet(matrix, weight, orthagonal = (weight == sqrt(2)))
    return Winverse * matrix * W

def wavelet(matrix, weight, orthagonal):
    W = Matrix(np.zeros(matrix.shape))
    i,j = matrix.indices(W.shape)
    factor = weight/2.
    W[2*i==j] = factor
    W[2*i==j-1] = factor
    W[2*i-W.shape[0]==j] = -factor
    W[2*i-W.shape[0]==j-1] = factor
    if orthagonal:
        Winverse = W.transpose()
    else:
        Winverse = W.inverse()
    return W, Winverse

def extransform ( matrix ):
    return Matrix( np.array( [ ( matrix[m+1] + matrix[m] ) / 2
                              for m in range( matrix.shape[0] - 1 ) ]
            + [ ( matrix[n+1] - matrix[n] ) / 2 
               for n in range( matrix.shape[0] - 1 ) ] ) )
    
def exinverse_transform ( matrix ):
    odd = [ matrix[n] - matrix[ n + matrix.shape[0] / 2 ]
    for n in range( matrix.shape[0] / 2 ) ]
    even = [ matrix[n] + matrix[ n + matrix.shape[0] / 2 ]
    for n in range( matrix.shape[0] / 2 ) ]
    inverselist = []
    for n in range(len(odd)):
        inverselist.append(odd[n])
        inverselist.append(even[n])
    return Matrix( np.array( inverselist ) )
