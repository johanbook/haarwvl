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
        
        # Read file and store in separate grayscale images
        arr = sm.imread(path)
        self._rows, self._cols, colors = arr.shape
        images = np.split(arr, colors, 2)
        self._images = []
        for image in images:
            self._images.append(Image(np.squeeze(image, axis=2).astype(float)))
        
    def _reform(self):
        """
        Returns an array with the image data (int format)
        """

        # make sure all pixels are inside of correct interval
        self.rectify()

        # extract pixel data
        arrays = []
        for image in self._images:
            arrays.append(image.matrix.array.reshape(self._rows, self._cols, 1))
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
        
    def display(self, title=None):
        """
        Displays the colored image. OBS: this will rectify the image which might introduce
        a (very) small data loss.
        """
        plt.figure()
        plt.imshow(self._reform())
        if title is not None:
            plt.title(title)
        plt.show()

    def invert(self):
        """
        Inverts each color of the image, ie. (r,g,b) -> (255-r, 255-g, 255-b).
        """
        for image in self._images:
            image.invert()

    def rectify(self):
        """
        Forces all pixels to the interval [0,255]
        """
        for image in self._images:
            image.rectify()

    def intensify(self, multiplier):
        """
        Increases the intensity of the image and clips all values outside of [0,255]
        """
        for image in self._images:
            image.intensify(multiplier)


# demonstration of rgb compression
# runs only if RRGImage is run as a module
if __name__ == '__main__':

    # create images to study
    path = '../res/group.jpg'
    a = RGBImage(path)
    b = RGBImage(path)
    a.display(title='Original')

    # compress a and show it
    a.compress()
    a.display(title='Compressed')

    # compress b and increase its intensity
    b.compress()
    b.intensify(64)
    b.display(title='Compressed with increased intensity')

    # uncompress a and display it
    a.uncompress()
    a.display(title='Uncompressed')
