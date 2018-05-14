# -*- coding: utf-8 -*-
#####################################################
# Image.py
# Günther
# bas12ban@student.lu.se
# 2018-05-10
#
# This class is gay and so am I
#####################################################

import os
import scipy.misc as sm
from scipy.misc import toimage
import matplotlib.pylab as plb

class Image:
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
        arr = sm.imread(path, True)
        
        rows, cols = arr.shape
        if rows % 2 != 0 : arr = arr[0:-1]
        if cols % 2 != 0 : arr = arr[:,0:-1]
        self.matrix = Matrix(arr)
        
    def save(self,path):
            sm.imsave(path, self.matrix.array)
            
    def compress(self,num=1, echo=False):
        self._num = num
        rows, cols = self.matrix.shape 
        
        if rows % 2**num != 0 or cols % 2**num != 0:
            print("WARNING: Significant compression artifacts might occur")
        
        
        if num < 1:
            raise Exception("Expected positive integer, got " + str(num))
        
        for n in range(num):
            temp_matrix = Matrix( self.matrix.array[0:int(rows/2**(n)),0:int(cols/2**(n))] )
                
            if echo:
                toimage(temp_matrix.array).show()

            temp_matrix = transform(temp_matrix)
           
            if echo: 
                print(temp_matrix.shape)
                print(matrix.shape)
            
            self.matrix.array[0:int(rows/2**n),0:int(cols/2**n)] = temp_matrix.array/2
            
            if echo:            
                print("Matrix max value:", np.amax( self.matrix.array))                            
        
    def uncompress(self, num=-1, echo=False):
        if num < 0:
            num = self._num
            
        for n in range(num-1,-1,-1):
            rows, cols = self.matrix.shape

            temp_matrix = Matrix( self.matrix.array[0:int(rows/2**n),0:int(cols/2**n)] )
                
            if echo:
                toimage(temp_matrix.array).show()
                
            temp_matrix = inverse_transform(temp_matrix)
            temp_matrix.array = 255*temp_matrix.array/np.amax(temp_matrix.array)
            self.matrix.array[0:int(rows/2**n),0:int(cols/2**n)] = temp_matrix.array
            
            if echo:            
                print("Matrix max value:", np.amax( self.matrix.array))
        
            
    
    def display(self):
        toimage(self.matrix.array).show()
    
      
    def invert(self, matrix):
        X, Y = matrix.shape
        for x in range(X):
            for y in range(Y):
                matrix.array[x][y] = 255 - matrix.array[x][y] 
        return matrix
