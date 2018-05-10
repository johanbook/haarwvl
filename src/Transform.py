# -*- coding: utf-8 -*-
"""
Created on Mon May  7 13:34:28 2018

@author: Frank Johansson
"""

import numpy as np
from scipy import *

def transform(matrix, weight = sqrt(2)):
    '''
    Compresses an image ( stored in 'matrix' ) using the Haar Wavelet Transformation method
    with a certain weight ( deafault sqrt(2) ).
    Returns the compressed image as a Matrix
    '''
    W, Winverse = wavelet(matrix, weight)
    return W * matrix * Winverse

def inverse_transform(matrix, weight = sqrt(2)):
    '''
    Uncompresses an image ( stored in 'matrix' ) using the Haar Wavelet Transformation method
    with a certain weight ( deafault sqrt(2) ).
    Returns the uncompressed image as a Matrix
    '''
    W, Winverse = wavelet(matrix, weight)
    return Winverse * matrix * W

def wavelet(matrix, weight):
    '''
    Constructs the Discrete Haar Wavelet Transformation matrix and its inverse.
    Depending on the chosen weight ( which determines whether the matrix is orthagonal ),
    the inverse is either set as the transpose or calculated normally.
    '''
    W = Matrix(np.zeros(matrix.shape))
    i,j = matrix.indices(W.shape)
    factor = weight/2.
    W[2*i==j] = factor
    W[2*i==j-1] = factor
    W[2*i-W.shape[0]==j] = -factor
    W[2*i-W.shape[0]==j-1] = factor
    if weight == sqrt(2):
        Winverse = W.transpose()
    else:
        Winverse = W.inverse()
    return W, Winverse

def extransform ( matrix ):
    '''
    Compresses an image ( stored in 'matrix' ) using the Haar Wavelet Transformation method.
    The calculations are made explicitly without the use of matrices.
    Returns the compressed image as a Matrix
    '''
    return Matrix( np.array( [ ( matrix[m+1] + matrix[m] ) / 2
                              for m in range( matrix.shape[0] - 1 ) ]
            + [ ( matrix[n+1] - matrix[n] ) / 2 
               for n in range( matrix.shape[0] - 1 ) ] ) )
    
def exinverse_transform ( matrix ):
    '''
    Uncompresses an image ( stored in 'matrix' ) using the Haar Wavelet Transformation method.
    The calculations are made explicitly without the use of matrices.
    Returns the uncompressed image as a Matrix
    '''
    odd = [ matrix[n] - matrix[ n + matrix.shape[0] / 2 ]
    for n in range( matrix.shape[0] / 2 ) ]
    even = [ matrix[n] + matrix[ n + matrix.shape[0] / 2 ]
    for n in range( matrix.shape[0] / 2 ) ]
    inverselist = []
    for n in range(len(odd)):
        inverselist.append(odd[n])
        inverselist.append(even[n])
    return Matrix( np.array( inverselist ) )
