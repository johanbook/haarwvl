# -*- coding: utf-8 -*-
#####################################################
# RGBImage.py
# Johan Book
# johanbook@hotmail.com
# 2018-05-12
#
# THIS CLASS DOES NOT WORK
# Extends an image to support colour.
#####################################################

import os
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as plt

from src.Image import Image


class RGBImage:
    def __init__(self, path):
        """
        An extension of Image.
        """
        
        # Check that path exists
        if not isinstance(path, str):
            raise TypeError('The path was not given as a string. Please put citation marks around the path.')
        if not os.path.exists(path):
            raise Exception('Path does not exist: ' + path)
        
        # default number of compressions
        # is used in uncompressed() if no argument is given
        self._num = 0        
        
        # Read file and store in separate grayscale images
        arr = sm.imread(path)
        rows, cols, colors = arr.shape
        images = np.split(arr, colors, 2)
        self._images = []
        for image in images:
            self._images.append(Image(np.squeeze(image, axis=2).astype(float)))
        
    def _reform(self):
        """
        Returns an array with the image data (int format)
        """
        r, c = self._images[0].matrix.array.shape
        arrays = []
        for image in self._images:
            arrays.append(image.matrix.array.reshape(r, c, 1))
        return np.concatenate(arrays, axis=2).astype(int)
            
    def compress(self, num=1):
        """
        Compresses the image.
        """
        for image in self._images:
            image.compress(num)
    
    def uncompress(self, num=1):
        """
        Uncompresses the image.
        """
        for image in self._images:
            image.uncompress(num)
        
    def display(self):
        """
        Displays the colored image.
        """
        plt.imshow(self._reform())
        plt.show()

    def invert(self):
        """
        Inverts each color of the image, ie. (r,g,b) -> (255-r, 255-g, 255-b).
        """
        for image in self._images:
            image.invert()


if __name__ == '__main__':
    path = '../res/group.jpg'
    a = RGBImage(path)
    a.display()

    a.compress(2)
    a.display()

    a.uncompress(2)
    a.display()
