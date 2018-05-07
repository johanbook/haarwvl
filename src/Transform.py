# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy import *

Matrix = array([[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]])

def transform(Matrix, weight = sqrt(1)):
    orthagonal = (weight == sqrt(2))
    W = np.zeros(Matrix.shape)
    i,j = np.indices(W.shape)
    W[2*i==j] = weight
    W[2*i==j-1] = weight
    W[2*i-W.shape[0]==j] = -weight
    W[2*i-W.shape[0]==j-1] = weight
    return W
