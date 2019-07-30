# -*- coding: utf-8 -*-
"""
Johan Book
johanbook@hotmail.com
2018-05-12

Extends an image to support colour.
"""

from PIL import Image
import os
import numpy as np

# import matplotlib.pyplot as plt

from .image import Image


class RGBImage:
    def __init__(self, input):
        """
        An extension of Image.
        """

        # Check that path exists
        if isinstance(input, str):
            if os.path.exists(input):
                arr = sm.imread(input)
            else:
                raise Exception("Path does not exist: " + input)
        elif isinstance(input, np.ndarray):
            arr = np.array(input)
        else:
            raise TypeError("Exepcted string or array, got:" + str(type(input)))

        # Read file and store each in a separate grayscale image
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

    def save(self, path):
        """
        Saves the image to specified path
        """
        sm.imsave(path, self._reform())

    def compress(self, num=1, explicit=False):
        """
        Compresses the image.
        """
        for image in self._images:
            image.compress(num, explicit=explicit)

    def uncompress(self, num=1, explicit=False):
        """
        Uncompresses the image.
        """
        for image in self._images:
            image.uncompress(num, explicit=explicit)

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

    def clone(self):
        """
        Returns a clone of this image.
        """
        return RGBImage(self._reform())
