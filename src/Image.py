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
        
        # comments
        self.path = path
        self.matrix = Matrix(sm.imread(self.path, True))
        self.reshape()
        
        # default number of compressions
        # is used in uncompressed() if no argument is given
        self._num = 0 
        
    def reshape(self):
        rows, cols = self.matrix.shape
        if rows % 2 != 0:
            self.matrix.array = self.matrix.array[0:-1]
        if cols % 2 != 0:
            self.matrix.array = self.matrix.array[:,0:-1]
        self.matrix = Matrix(self.matrix.array)
        
    def save(self,path):
            sm.imsave(path, self.matrix.array)
            
    def compress(self,num=1, echo=False):
        #self.matrix = transform(self.matrix)
        self._num = num
        if num >= 1:
            for n in range(num):
                rows, cols = shape(self.matrix.array)
                #print(rows,cols)
                temp_matrix = Matrix( self.matrix.array[0:rows/2**(n),0:cols/2**(n)] )
                
                if echo:
                    toimage(temp_matrix.array).show()
                
                #print(shape(temp_matrix.array))
                temp_matrix = transform(temp_matrix)
                #self.matrix = temp_matrix
                #toimage(self.invert(temp_matrix).array).show()
                self.matrix.array[0:rows/2**(n),0:cols/2**(n)] = temp_matrix.array
                #toimage(self.invert(temp_matrix).array).show()
                self.matrix = Matrix( self.matrix.array )                
                
    def uncompress(self, num=-1):
        if num < 0:
            num = self._num
        
        
            
        self.matrix = inverse_transform(self.matrix)
    
    def display(self):
        toimage(self.matrix.array).show()
    
      
    def invert(self, matrix):
        X, Y = matrix.shape
        for x in range(X):
            for y in range(Y):
                matrix.array[x][y] = 255 - matrix.array[x][y] 
        return matrix
