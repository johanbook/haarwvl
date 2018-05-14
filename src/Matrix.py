#####################################################
# Matrix.py
# David Linehan
# nat13dli@student.lu.se 
# 2018-05-09
#####################################################

import numpy as np

class Matrix:

    def __init__(self, array):
        if not isinstance(array, np.ndarray):
            raise TypeError('Expected a numpy array as argument.')
            
        self.array = array
        
    def __add__(self, other):
        return Matrix(self.array+other.array)
        
    def __sub__(self, other):
        return Matrix(self.array-other.array)
        
    def __mul__(self, other):
        return Matrix(np.dot(self.array,other.array))
        
    def __pow__(self, other):
        return Matrix(self.array**other.array)
        
    def inverse(self):
        return Matrix(np.linalg.inv(self.array))
        
    def transpose(self):
        return Matrix(np.matrix.transpose(self.array))
        
    def __repr__(self):
        s = ""
        for x in self.array:
            s+='\n'+str(x)
        return s+'\n'    
    
    @property
    def shape(self):
        return array.shape
        
    def indices(self):
        return np.indices(self.shape)
