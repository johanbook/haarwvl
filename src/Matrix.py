# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:35:12 2018
@author: dvdli
"""
import numpy as np

class Matrix:

    def __init__(self, array):
        if not isinstance(array, ndarray):
            raise TypeError('Expected a numpy array as argument.')
        self.array = array
        self.shape = self.array.shape
        
    def __add__(self, other):
        return Matrix(self.array+other.array)
        
    def __sub__(self, other):
        return Matrix(self.array-other.array)
        
    def __mul__(self, other):
        return Matrix(dot(self.array,other.array))
        
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
        
    def indices(self):
        return np.indices(self.shape)
        
    def array(self):
        return self.array    
