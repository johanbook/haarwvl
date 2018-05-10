# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:34:56 2018

@author: bas12ban
"""

import os
import scipy.misc as sm

class Image:
    def __init__(self,path=None):
        '''
        Input: path (string) provided by user, given in one of the two following forms, ex1: 'C:\\users\\documents' or ex2: 'C:/users/documents', if these forms are ignored, nothing will work.
        '''
        
        if path == None:
            raise Exception('No path was given.')
        elif not isinstance(path,str):
            raise TypeError('The path was not given as a string. Please put citation marks around the path.')
        elif os.path.exists(path) == False:
            raise Exception('Path does not exist. Try again.')
        self.path = path        
        
    def importim(self):
            return sm.imread(self.path, True)
        
    def save(self):
            im_array = self.importim()
            sm.imsave('newimagefile.jpg', im_array)
