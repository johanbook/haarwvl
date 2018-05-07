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
