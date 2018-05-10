# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:34:56 2018

@author: bas12ban
"""

import os
import scipy.misc as sm
from scipy.misc import toimage


class Image:
    def __init__(self,path=None):
        '''
        Class representing an grayscale image. Imported images can be compressed using the Haar Wavelet transformation, compressed images can be uncompressed.
        Input: path (string) provided by user, given in one of the two following forms, ex1: 'C:\\users\\documents' or ex2: 'C:/users/documents', if these forms are ignored, nothing will work.
        '''        
        if path == None:
            raise Exception('No path was given.')
        elif not isinstance(path,str):
            raise TypeError('The path was not given as a string. Please put citation marks around the path.')
        elif os.path.exists(path) == False:
            raise Exception('Path does not exist. Try again.')
        self.path = path
        self.matrix = Matrix(sm.imread(self.path, True))
        self.reshape()
        
    def reshape(self):
        rows, cols = self.matrix.shape
        if rows % 2 != 0:
            self.matrix.array = self.matrix.array[0:-1]
        if cols % 2 != 0:
            self.matrix.array = self.matrix.array[:,0:-1]
        
        
    def save(self):
            sm.imsave('newimagefile.jpg', self.matrix)
            
    def compress(self,num=1):
        self.matrix = self.matrix *0
    
    def display(self):
        toimage(self.matrix.array).show()
    
    
