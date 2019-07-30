# -*- coding: utf-8 -*-
"""
Created on Mon May  7 13:34:28 2018
@author: Frank Johansson
"""

from math import sqrt
import numpy as np


def transform(matrix):
    """
    (Frank Johansson, nat13fjo@student.lu.se)
    Compresses an image ( stored in 'matrix' )
    using the Haar Wavelet Transformation method.
    Returns the compressed image as a Matrix
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError(f"Expected numpy array but got {type(matrix)}")
    Wm, Wn = _wavelet(matrix)
    Wn = Wn.transpose()
    return Wm * matrix * Wn


def inverse_transform(matrix):
    """
    Uncompresses an image ( stored in 'matrix' )
    using the Haar Wavelet Transformation method.
    Returns the uncompressed image as a Matrix
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError(f"Expected numpy array but got {type(matrix)}")
    Wm, Wn = _wavelet(matrix)
    Wm = Wm.transpose()
    return Wm * matrix * Wn


def _wavelet(matrix):
    """
    Constructs the Discrete Haar Wavelet Transformation matrices,
    compatible with the argument matrix, and returns them.
    """

    # Initialize transformation matrices
    Wm = np.zeros((matrix.shape[0], matrix.shape[0]))
    Wn = np.zeros((matrix.shape[1], matrix.shape[1]))

    # Create indices for element assignment
    i, j = np.indices(Wm.shape)
    k, l = np.indices(Wn.shape)

    # The factor to set the transformation matrix element to
    factor = sqrt(2) / 2.0

    # Finalize the LHS transformation matrix
    Wm[2 * i == j] = factor
    Wm[2 * i == j - 1] = factor
    Wm[2 * i - Wm.shape[0] == j] = -factor
    Wm[2 * i - Wm.shape[0] == j - 1] = factor

    # Finalize the RHS transformation matrix
    Wn[2 * k == l] = factor
    Wn[2 * k == l - 1] = factor
    Wn[2 * k - Wn.shape[0] == l] = -factor
    Wn[2 * k - Wn.shape[0] == l - 1] = factor

    # Return the LHS and the RHS transformation matrices
    return Wm, Wn


def extransform(matrix):
    """
    Compresses an image ( stored in 'matrix' )
    using the Haar Wavelet Transformation method.
    The calculations are made explicitly without the use of matrices.
    Returns the compressed image as a Matrix
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError(f"Expected numpy array but got {type(matrix)}")

    # Create useful variables
    a, b = int(matrix.shape[0] / 2), int(matrix.shape[1] / 2)

    # Initialize transformed matrices for
    # the four quadrants and assign elements
    topleft = np.zeros((a, b))
    topright = np.zeros((a, b))
    bottomleft = np.zeros((a, b))
    bottomright = np.zeros((a, b))
    for m in range(int(matrix.shape[0] / 2)):
        for n in range(int(matrix.shape[1] / 2)):
            topleft[m][n] = (
                matrix[2 * m][2 * n]
                + matrix[2 * m][2 * n + 1]
                + matrix[2 * m + 1][2 * n]
                + matrix[2 * m + 1][2 * n + 1]
            ) / 2
            topright[m][n] = (
                -matrix[2 * m][2 * n]
                + matrix[2 * m][2 * n + 1]
                - matrix[2 * m + 1][2 * n]
                + matrix[2 * m + 1][2 * n + 1]
            ) / 2
            bottomleft[m][n] = (
                -matrix[2 * m][2 * n]
                - matrix[2 * m][2 * n + 1]
                + matrix[2 * m + 1][2 * n]
                + matrix[2 * m + 1][2 * n + 1]
            ) / 2
            bottomright[m][n] = (
                -matrix[2 * m][2 * n]
                + matrix[2 * m][2 * n + 1]
                + matrix[2 * m + 1][2 * n]
                - matrix[2 * m + 1][2 * n + 1]
            ) / 2

    # Combine the quadrants and return the transformed matrix
    return np.vstack(
        (np.hstack((topleft, topright)), np.hstack((bottomleft, bottomright)))
    )


def exinverse_transform(matrix):
    """
    Uncompresses an image ( stored in 'matrix' )
    using the Haar Wavelet Transformation method.
    The calculations are made explicitly without the use of matrices.
    Returns the uncompressed image as a Matrix
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError(f"Expected numpy array but got {type(matrix)}")

    # Create useful variables
    a, b = int(matrix.shape[0]), int(matrix.shape[1])
    c, d = int(a / 2), int(b / 2)

    # Initialize transformed matrix and assign elements
    transformed = np.zeros((a, b))
    for m in range(c):
        for n in range(d):
            transformed[2 * m][2 * n] = (
                matrix[m][n]
                - matrix[m][n + d]
                - matrix[m + c][n]
                - matrix[m + c][n + d]
            ) / 2
            transformed[2 * m][2 * n + 1] = (
                matrix[m][n]
                + matrix[m][n + d]
                - matrix[m + c][n]
                + matrix[m + c][n + d]
            ) / 2
            transformed[2 * m + 1][2 * n] = (
                matrix[m][n]
                - matrix[m][n + d]
                + matrix[m + c][n]
                + matrix[m + c][n + d]
            ) / 2
            transformed[2 * m + 1][2 * n + 1] = (
                matrix[m][n]
                + matrix[m][n + d]
                + matrix[m + c][n]
                - matrix[m + c][n + d]
            ) / 2

    return transformed
