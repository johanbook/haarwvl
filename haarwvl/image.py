# -*- coding: utf-8 -*-
"""
Björn Annby - Andersson
bas12ban@student.lu.se
2018-05-10

Class called Image.
"""

from PIL import Image as PILImage
import os


from .transform import *


class Image:
    """
    Image that can be compressed and uncompressed using the Haar Wavelet
    transformation.

    Args:
        image (str or np.array): The image.
    """

    def __init__(self, array):
        if isinstance(array, str):
            if os.path.exists(array):
                array = np.array(PILImage.open(array))
            else:
                raise Exception(f"Path does not exist: {array}")
        if not isinstance(array, np.ndarray):
            raise TypeError(f"Expected string or array, got {type(array)}")

        # default number of compressions
        # is used in uncompressed() if no argument is given
        self._num = 0

        # If the number of rows or columns of "arr" is odd, "arr" is reshaped to be an
        # array of even number of columns and rows.
        rows, cols = array.shape
        if rows % 2 != 0:
            array = array[0:-1]
        if cols % 2 != 0:
            array = array[:, 0:-1]
        self.array = array

    def save(self, path):
        """
        Save image to disc.

        Args:
            path (str): Where to save image.
        """
        image = PILImage.fromarray(self.array)
        if image.mode != "RGB":
            image = image.convert("RGB")
        image.save(path)

    def compress(self, num=1, explicit=False):
        """
         Compress image using a Haar wavelet transformation.

         Args:
             num (int): Number of times to apply compression (default 1).
             explicit (bool) If true, compression will use explicit
                form of transformation (default False).
        """
        if num < 1:
            raise Exception(f"Expected positive integer, got {num}")

        self._num = num
        rows, cols = self.array.shape

        if rows % 2 ** num != 0 or cols % 2 ** num != 0:
            print("WARNING: Significant compression artifacts might occur")

        for n in range(num):
            temp_matrix = self.array[0 : int(rows / 2 ** n), 0 : int(cols / 2 ** n)]

            temp_matrix = (
                extransform(temp_matrix) if explicit else transform(temp_matrix)
            )

            self.array[0 : int(rows / 2 ** n), 0 : int(cols / 2 ** n)] = temp_matrix / 2

        return self

    def uncompress(self, num=-1, explicit=False):
        """
         Uncompress image using a Haar wavelet transformation.

         Args:
             num (int): Number of times to apply uncompression (default 1).
             explicit (bool) If true, compression will use explicit
                form of transformation (default False).
        """
        if num < 0:
            num = self._num

        for n in range(num - 1, -1, -1):
            rows, cols = self.array.shape

            temp_matrix = self.array[0 : int(rows / 2 ** n), 0 : int(cols / 2 ** n)]

            temp_matrix = (
                exinverse_transform(temp_matrix)
                if explicit
                else inverse_transform(temp_matrix)
            )
            temp_matrix = 255 * temp_matrix / np.amax(temp_matrix)
            self.array[0 : int(rows / 2 ** n), 0 : int(cols / 2 ** n)] = temp_matrix

        return self

    def show(self):
        """
        Display the image.
        """
        PILImage(self.array).show()

    def invert(self):
        """
        Inverts the pixel coefficients of the image.
        """
        self.array = 255 - self.array

    def rectify(self):
        """
        Forces all pixels to the interval [0, 255]
        """
        self.array[self.array < 0] = 0
        self.array[self.array > 255] = 255

    def intensify(self, multiplier):
        """
        Increases the intensity of the image and clips all values outside of [0,255]
        """
        self.array *= multiplier
        self.rectify()

    def clone(self):
        """
        Returns a copy of the image.
        """
        image = Image(self.array)
        image._num = self._num
        return image
