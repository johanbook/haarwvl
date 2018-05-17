# -*- coding: utf-8 -*-
"""
Created on Mon May  7 13:34:28 2018
@author: Frank Johansson
"""

import numpy as np
from scipy import *

def transform(matrix):
    '''
    (Frank Johansson, nat13fjo@student.lu.se)
    Compresses an image ( stored in 'matrix' )
    using the Haar Wavelet Transformation method.
    Returns the compressed image as a Matrix
    '''
    
    # Check if the argument is a Matrix,
    # creates the transformation matrices
    # and performs the transformation
    if not isinstance(matrix, Matrix):
       raise TypeError ('Expects an image as a Matrix. Got:', type(matrix))
    Wm, Wn = wavelet(matrix)
    Wn = Wn.transpose()
    return Wm * matrix * Wn

def inverse_transform(matrix):
    '''
    (Frank Johansson, nat13fjo@student.lu.se)
    Uncompresses an image ( stored in 'matrix' )
    using the Haar Wavelet Transformation method.
    Returns the uncompressed image as a Matrix
    '''
    
    # Check if the argument is a Matrix,
    # creates the transformation matrices
    # and performs the transformation
    if not isinstance(matrix, Matrix):
        raise TypeError ('Expects an image as a Matrix. Got:', type(matrix) )
    Wm, Wn = wavelet(matrix)
    Wm = Wm.transpose()
    return Wm * matrix * Wn

def wavelet(matrix):
    '''
    (Frank Johansson, nat13fjo@student.lu.se)
    Constructs the Discrete Haar Wavelet Transformation matrices,
    compatible with the argument matrix, and returns them.
    '''
    
    # Initialize transformation matrices
    Wm = Matrix(np.zeros((matrix.shape[0],matrix.shape[0])))
    Wn = Matrix(np.zeros((matrix.shape[1],matrix.shape[1])))

    # Create indices for element assignment
    i,j = Wm.indices()
    k,l = Wn.indices()    
    
    # The factor to set the transformation matrix element to
    factor = sqrt(2)/2.
    
    # Finalize the LHS transformation matrix
    Wm.array[2*i==j] = factor
    Wm.array[2*i==j-1] = factor
    Wm.array[2*i-Wm.shape[0]==j] = -factor
    Wm.array[2*i-Wm.shape[0]==j-1] = factor
    
    # Finalize the RHS transformation matrix
    Wn.array[2*k==l] = factor
    Wn.array[2*k==l-1] = factor
    Wn.array[2*k-Wn.shape[0]==l] = -factor
    Wn.array[2*k-Wn.shape[0]==l-1] = factor
    
    # Return the LHS and the RHS transformation matrices
    return Wm, Wn

def extransform ( matrix ):
    '''
    (Frank Johansson, nat13fjo@student.lu.se)
    Compresses an image ( stored in 'matrix' )
    using the Haar Wavelet Transformation method.
    The calculations are made explicitly without the use of matrices.
    Returns the compressed image as a Matrix
    '''
    # Check if the argument is a Matrix,
    # construct the transformation by adding two lists
    # and use the result to create a matrix
    if not isinstance(matrix, Matrix):
        raise TypeError ('Expects an image as a Matrix. Got:', type(matrix) )
    a, b = int(matrix.shape[0] / 2), int(matrix.shape[1] / 2)
    topleft = np.zeros((a,b))
    topright = np.zeros((a,b))
    bottomleft = np.zeros((a,b))
    bottomright = np.zeros((a,b))
    for m in range(int(matrix.shape[0]/2)):
        for n in range(int(matrix.shape[1]/2)):
            topleft[m][n] = ( matrix.array[2*m][2*n] + matrix.array[2*m][2*n+1] 
                               + matrix.array[2*m+1][2*n] + matrix.array[2*m+1][2*n+1]) / 2
            topright[m][n] = ( -matrix.array[2*m][2*n] + matrix.array[2*m][2*n+1] 
                               - matrix.array[2*m+1][2*n] + matrix.array[2*m+1][2*n+1]) / 2
            bottomleft[m][n] = ( -matrix.array[2*m][2*n] - matrix.array[2*m][2*n+1] 
                               + matrix.array[2*m+1][2*n] + matrix.array[2*m+1][2*n+1]) / 2
            bottomright[m][n] = ( -matrix.array[2*m][2*n] + matrix.array[2*m][2*n+1] 
                               + matrix.array[2*m+1][2*n] - matrix.array[2*m+1][2*n+1]) / 2
    return Matrix(np.vstack((np.hstack((topleft,topright)),np.hstack((bottomleft,bottomright)))))
    
def exinverse_transform ( matrix ):
    '''
    (Frank Johansson, nat13fjo@student.lu.se)
    Uncompresses an image ( stored in 'matrix' )
    using the Haar Wavelet Transformation method.
    The calculations are made explicitly without the use of matrices.
    Returns the uncompressed image as a Matrix
    '''
    
    # Check if the argument is a Matrix
    if not isinstance(matrix, Matrix):
        raise TypeError ('Expects an image as a Matrix. Got:', type(matrix) )
    a, b = int(matrix.shape[0]), int(matrix.shape[1])
    c, d = int(a/2) , int(b/2)
    transformed = np.zeros((a, b))
    for m in range(c):
        for n in range(d):
            transformed[2*m][2*n] = (matrix.array[m][n] - 
                                    matrix.array[m][n+c] -
                                    matrix.array[m+d][n] -
                                    matrix.array[m+c][n+d]) / 2
            transformed[2*m][2*n+1] = (matrix.array[m][n] + 
                                        matrix.array[m][n+d] -
                                        matrix.array[m+c][n] +
                                        matrix.array[m+c][n+d]) / 2
            transformed[2*m+1][2*n] = (matrix.array[m][n] - 
                                        matrix.array[m][n+d] +
                                        matrix.array[m+c][n] +
                                        matrix.array[m+c][n+d]) / 2
            transformed[2*m+1][2*n+1] = (matrix.array[m][n] + 
                                        matrix.array[m][n+d] +
                                        matrix.array[m+c][n] -
                                        matrix.array[m+c][n+d]) / 2

    return Matrix(transformed)
