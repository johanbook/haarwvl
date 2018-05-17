# -*- coding: utf-8 -*-
#####################################################
# Image.py
# Björn Annby - Andersson
# bas12ban@student.lu.se
# 2018-05-10
#
# Class called Image.
#####################################################

import os
import numpy as np
import scipy.misc as sm
from scipy.misc import toimage

from src.Matrix import Matrix
from src.Transform import *


class Image:
    def __init__(self, input):
        """
        (Björn Annby-Andersson, bas12ban@student.lu.se
         Johan Book, nat13jbo@student.lu.se)
        Class representing an grayscale image. Imported images can be compressed 
        using the Haar Wavelet transformation, compressed images can be uncompressed.
        Input: path (string) provided by user, given in one of the two following forms, 
        ex1: 'C:\\users\\documents' or ex2: 'C:/users/documents'.
        """

        # The if statements check whether the path is given as a string or if the path exists. Raises errors when
        # the path is not given as a string or if the path does not exist. 
        if isinstance(input, str):
            if os.path.exists(input):
                arr = sm.imread(input, True)
            else:
                raise Exception('Path does not exist: ' + input)
        elif isinstance(input, np.ndarray):
            arr = input
        else:
            raise TypeError('Expected string or array, got' + str(type(input)))

        # default number of compressions
        # is used in uncompressed() if no argument is given
        self._num = 0        

        # If the number of rows or columns of "arr" is odd, "arr" is reshaped to be an
        # array of even number of columns and rows.
        rows, cols = arr.shape
        if rows % 2 != 0:
            arr = arr[0:-1]
        if cols % 2 != 0:
            arr = arr[:, 0:-1]
        self.matrix = Matrix(arr)
        
    def save(self, path):
        """
        (Björn Annby-Andersson, bas12ban@student.lu.se)
        This method takes a path as input and stores the matrix 
        representation of an image as a grayscale picture at the given path.
        Input: path (string), provided by user.
        """
        sm.imsave(path, self.matrix.array)
            
    def compress(self, num=1, echo=False, explicit=False):
        """
        (Björn Annby-Andersson, bas12ban@student.lu.se
         Johan Book, nat13jbo@student.lu.se)
         Compresses an image with the Haar wavelet transformation.
         Inputs: num (int), number of compressions, given by user (default value is 1)
                 echo (Boolean), should not be specified by user (default False)
        """
        self._num = num
        rows, cols = self.matrix.shape 
        
        if rows % 2**num != 0 or cols % 2**num != 0:
            print("WARNING: Significant compression artifacts might occur")

        if num < 1:
            raise Exception("Expected positive integer, got " + str(num))
        
        for n in range(num):
            temp_matrix = Matrix(self.matrix.array[0:int(rows/2**n), 0:int(cols/2**n)])
                
            if echo:
                toimage(temp_matrix.array).show()

            temp_matrix = extransform(temp_matrix) if explicit else transform(temp_matrix)
           
            if echo: 
                print(temp_matrix.shape)
            
            self.matrix.array[0:int(rows/2**n), 0:int(cols/2**n)] = temp_matrix.array/2
            
            if echo:            
                print("Matrix max value:", np.amax(self.matrix.array))
        
    def uncompress(self, num=-1, echo=False, explicit=False):
        """
        (Björn Annby-Andersson, bas12ban@student.lu.se
         Johan Book, nat13jbo@student.lu.se)
         Decompresses a compressed image. User must know how many times the input image is compressed
         to get back original.
         Inputs: num (int), number of times to decompress, provided by user 
                 echo (Boolean), should not be used by user (default False)
        """
        if num < 0:
            num = self._num
            
        for n in range(num-1, -1, -1):
            rows, cols = self.matrix.shape

            temp_matrix = Matrix(self.matrix.array[0:int(rows/2**n), 0:int(cols/2**n)])
                
            if echo:
                toimage(temp_matrix.array).show()
                
            temp_matrix = exinverse_transform(temp_matrix) if explicit else inverse_transform(temp_matrix)
            temp_matrix.array = 255*temp_matrix.array/np.amax(temp_matrix.array)
            self.matrix.array[0:int(rows/2**n), 0:int(cols/2**n)] = temp_matrix.array
            
            if echo:            
                print("Matrix max value:", np.amax(self.matrix.array))

    def display(self):
        """
        (Björn Annby - Andersson, bas12ban@student.lu.se)
        This method displays the current version of the image, it can be compressed, decompressed or neither. 
        """
        toimage(self.matrix.array).show()

    def invert(self):
        """
        (Johan Book, nat13jbo@student.lu.se)
        Inverts the gray-scale coefficients of the image.
        """
        xlim, ylim = self.matrix.shape
        for x in range(xlim):
            for y in range(ylim):
                self.matrix.array[x][y] = 255 - self.matrix.array[x][y]


if __name__ == '__main__':
    path = '../res/group.jpg'
    a = Image(path)
    a.display()

    a.compress()
    a.uncompress()

    a.display()
