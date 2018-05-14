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
#    if not isinstance(matrix, Matrix):
#       raise TypeError ('Expects an image as a Matrix. Got:', type(matrix))
    Wm, Wn = wavelet(matrix)
    Wn = Wn.transpose()
    #return Wm * matrix * Wn # Comment out for testing
    return np.dot(Wm, np.dot(matrix,Wn)) # Uncomment for testing

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
#    if not isinstance(matrix, Matrix):
#        raise TypeError ('Expects an image as a Matrix. Got:', type(matrix) )
    Wm, Wn = wavelet(matrix)
    Wm = Wm.transpose()
    #return Wm * matrix * Wn # Comment out for testing
    return np.dot(Wm, np.dot(matrix,Wn)) # Uncomment for testing

def wavelet(matrix):
    '''
    (Frank Johansson, nat13fjo@student.lu.se)
    Constructs the Discrete Haar Wavelet Transformation matrices,
    compatible with the argument matrix, and returns them.
    '''
    
#    # Initialize transformation matrices, comment out for testing
#    Wm = Matrix(np.zeros((matrix.shape[0],matrix.shape[0])))
#    Wn = Matrix(np.zeros((matrix.shape[1],matrix.shape[1])))
#
#    # Create indices for element assignment
#    i,j = Wm.indices()
#    k,l = Wn.indices()    
    # Initialize transformation matrices, uncomment for testing
    Wm = np.zeros((matrix.shape[0],matrix.shape[0]))
    Wn = np.zeros((matrix.shape[1],matrix.shape[1]))
    
    #Create indices for element assignment
    i,j = np.indices(Wm.shape)
    k,l = np.indices(Wn.shape) 
    
    # The factor to set the transformation matrix element to
    factor = sqrt(2)/2.
#    
#    # Finalize the LHS transformation matrix
#    Wm.array[2*i==j] = factor
#    Wm.array[2*i==j-1] = factor
#    Wm.array[2*i-Wm.shape[0]==j] = -factor
#    Wm.array[2*i-Wm.shape[0]==j-1] = factor
#    
#    # Finalize the RHS transformation matrix
#    Wn.array[2*k==l] = factor
#    Wn.array[2*k==l-1] = factor
#    Wn.array[2*k-Wn.shape[0]==l] = -factor
#    Wn.array[2*k-Wn.shape[0]==l-1] = factor

        
    # Finalize the LHS transformation matrix
    Wm[2*i==j] = factor
    Wm[2*i==j-1] = factor
    Wm[2*i-Wm.shape[0]==j] = -factor
    Wm[2*i-Wm.shape[0]==j-1] = factor
    
    # Finalize the RHS transformation matrix
    Wn[2*k==l] = factor
    Wn[2*k==l-1] = factor
    Wn[2*k-Wn.shape[0]==l] = -factor
    Wn[2*k-Wn.shape[0]==l-1] = factor
    
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
    return Matrix( np.array( [ ( matrix[m+1] + matrix[m] ) / 2
                              for m in range( matrix.shape[0] - 1 ) ]
                            + [ ( matrix[n+1] - matrix[n] ) / 2 
                               for n in range( matrix.shape[0] - 1 ) ] ) )
    
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
        
    # Construct the odd indexed elements
    odd = [ matrix[n] - matrix[ n + matrix.shape[0] / 2 ]
            for n in range( matrix.shape[0] / 2 ) ]
    
    # Construct the even indexed elements
    even = [ matrix[n] + matrix[ n + matrix.shape[0] / 2 ]
        for n in range( matrix.shape[0] / 2 ) ]
    
    # Add the odd and even elements alternatingly
    # to create the transformed matrix
    inverselist = []
    for n in range(len(odd)):
        inverselist.append(odd[n])
        inverselist.append(even[n])
    return Matrix( np.array( inverselist ) )

# Test file methods

a = np.array([[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],
              [1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]])
for n in range(num):
    rows, cols = shape(self.matrix.array)
    #print(rows,cols)
    temp_matrix = Matrix( self.matrix.array[0:rows/2**(n),0:cols/2**(n)] )
                
    #print(shape(temp_matrix.array))
    temp_matrix = transform(temp_matrix)
    #self.matrix = temp_matrix
    #toimage(self.invert(temp_matrix).array).show()
    self.matrix.array[0:rows/2**(n),0:cols/2**(n)] = temp_matrix.array
    #toimage(self.invert(temp_matrix).array).show()
    self.matrix = Matrix( self.matrix.array )   
