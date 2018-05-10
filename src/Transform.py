# -*- coding: utf-8 -*-
"""
Created on Mon May  7 13:34:28 2018

@author: Frank Johansson
"""

import numpy as np
from scipy import *

def _isnumber(x):
    return isinstance(x, int) or isinstance(x, float)

def _inverse(matrix, weight):
    if weight == sqrt(2):
        Winverse = matrix.transpose()
    else:
        Winverse = martix.inverse()
    return Winverse

def transform(matrix, weight = sqrt(2)):
    '''
    Compresses an image ( stored in 'matrix' ) using the Haar Wavelet Transformation method
    with a certain weight ( deafault sqrt(2) ).
    Returns the compressed image as a Matrix
    '''
    if isinstance(matrix, Matrix):
        if _isnumber(weight):
            Wm, Wn = wavelet(matrix, weight)
            Wn = _inverse(Wn, weight)
            return Wm * matrix * Wn
        else:
            raise TypeError ('Expects a real number weight.')
    else:
        raise TypeError ('Expects an image as a Matrix.')

def inverse_transform(matrix, weight = sqrt(2)):
    '''
    Uncompresses an image ( stored in 'matrix' ) using the Haar Wavelet Transformation method
    with a certain weight ( deafault sqrt(2) ).
    Returns the uncompressed image as a Matrix
    '''
    if isinstance(matrix, Matrix):
        if _isnumber(weight):
            Wm, Wn = wavelet(matrix, weight)
            Wm = _inverse(Wm, weight)
            return Wm * matrix * Wn
        else:
            raise TypeError ('Expects a real number weight.')
    else:
        raise TypeError ('Expects an image as a Matrix.')
    

def wavelet(matrix, weight):
    '''
    Constructs the Discrete Haar Wavelet Transformation matrix and its inverse.
    Depending on the chosen weight ( which determines whether the matrix is orthagonal ),
    the inverse is either set as the transpose or calculated normally.
    '''
    Wm = Matrix(np.zeros((matrix.shape[0],matrix.shape[0])))
    Wn = Matrix(np.zeros((matrix.shape[1],matrix.shape[1])))
    i,j = matrix.indices(Wm.shape)
    k,l = matrix.indices(Wn.shape)
    factor = weight/2.
    Wm[2*i==j] = factor
    Wm[2*i==j-1] = factor
    Wm[2*i-Wm.shape[0]==j] = -factor
    Wm[2*i-Wm.shape[0]==j-1] = factor
    Wn[2*k==l] = factor
    Wn[2*k==l-1] = factor
    Wn[2*k-Wn.shape[0]==l] = -factor
    Wn[2*k-Wn.shape[0]==l-1] = factor
    return Wm, Wn

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
