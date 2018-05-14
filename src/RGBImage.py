# -*- coding: utf-8 -*-
#####################################################
# Test.py
# Johan Book
# johanbook@hotmail.com
# 2018-05-07
#
# Methods to probe the performance of the rest of
# the package.
# Methods:
# - test_matrix() : tests the matrix class
# - test_image()  : tests the image class 
# If this module is run as a script both of these
# methods will be callled.
#####################################################

import os
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as plt
from scipy.misc import toimage

class RGBImage:
    def __init__(self, path):
        '''
        Class representing an grayscale image. Imported images can be compressed 
        using the Haar Wavelet transformation, compressed images can be uncompressed.
        Input: path (string) provided by user, given in one of the two following forms, 
        ex1: 'C:\\users\\documents' or ex2: 'C:/users/documents', if these forms are ignored, nothing will work.
        '''        
        
        # comments
        if not isinstance(path,str):
            raise TypeError('The path was not given as a string. Please put citation marks around the path.')
        if not os.path.exists(path):
            raise Exception('Path does not exist: ' + path)
        
        # default number of compressions
        # is used in uncompressed() if no argument is given
        self._num = 0        
        
        # comments
        arr = sm.imread(path)
        rows, cols, colors = arr.shape
        imgs= np.split(arr,colors,2)
        self._images = []
        for img in imgs:
            self._images.append(Image(np.squeeze(img, axis=2)))
        
    def _reform(self):
        r,c = self._images[0].matrix.array.shape
        arrs = []
        for image in self._images:
            arrs.append(image.matrix.array) 
        return np.concatenate(arrs).reshape(r,c,len(self._images))
            
    def compress(self, num=1):
        for image in self._images:
            image.compress(num)
    
    def uncompress(self, num=1):
        for image in self._images:
            image.uncompress(num)
        
    def display(self):
        toiamge(self._reform).show()
        
    def invert():
        for image in self._images:
            image.invert()
