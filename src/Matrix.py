# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:35:12 2018

@author: dvdli
"""
from  scipy import *
from  pylab import *
from  scipy.integrate import quad
import numpy as np

class Matrix:


    def __init__(self, array):
        self.array = array
        
        
    def __add__(self, other):
        return self.array+other.array
        
    def __sub__(self, other):
        return self.array-other.array
        
    def __mul__(self, other):
        return self.array*other.array
        
    def __pow__(self, other):
        returnself.array**other.array
        
    def inverse(self):
        return np.linalg.inv(self.array)
        
    def transpose(self):
        return np.matrix.transpose(self.array)
        
    def __rep__(self):
        return string(self.array)
        
    def shape(self):
        return np.ndarray.shape(self.array)
        
    def indices(self):
        return np.indices(self.array)
        
    def array(self):
        return self.array
        
        