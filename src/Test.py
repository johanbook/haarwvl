# -*- coding: utf-8 -*-
#####################################################
# Test.py
# Johan Book
# johanbook@hotmail.com
# 2018-05-07
#
# Methods to probe the performance of the rest of
# the package.
# Classes:
# - TestMatrix          : Matrix class
# - TestImage           : Image class 
# - TestTransformation  : Transformation class
# If this module is run as a script all unittests in 
# these classes will be run.
#####################################################

import numpy as np
import unittest
import os

from src.Matrix import Matrix
from src.Image import Image
from src.Transform import *

PATH = '../res/python.jpg'


# Test matrix class
class TestMatrix(unittest.TestCase):
    def test_arithmetics(self):
        i = Matrix(np.eye(2))
        # self.assertAlmostEqual
    
    def test_inverse(self):
        dim = 3
        a = Matrix(np.random.rand(dim, dim))
        i = a*a.inverse() 
        q = np.sum(i.array - np.eye(dim))
  
        self.assertAlmostEqual(q, 0)
        
    def test_transpose(self):
        pass


# Test image class
class TestImage(unittest.TestCase):
    def test_badinput(self):
        self.assertRaises(Exception, Image, None)
    
    @unittest.skipIf(not os.path.exists(PATH), 'Test file does not exist: '+PATH)
    def test_compression(self):
        # Load image
        image = Image(PATH)
        b = np.array(image.matrix.array)

        # Compress and Uncompress
        image.compress(4)
        image.uncompress(4)
        c = np.array(image.matrix.array)
  
        # Estimate MAE error
        err = abs(b-c)
        err = sum(err)/len(err)

        # The error can be large even though the image is fine
        self.assertLessEqual(err, 1.e+3)
      
    @unittest.skipIf(not os.path.exists(PATH), 'Test file does not exist: '+PATH)
    def test_save(self):
        test_path = '../test.png'
        image = Image(PATH)
        try:
            image.save(test_path)
        except Exception:
            self.assertTrue(False)

        if os.path.exists(test_path):
            os.remove(test_path)
        else:
            self.assertTrue(False)


# Transformation class
class TestTransformation(unittest.TestCase):
    def _generate_matrix():
        return Matrix(np.random.rand(8, 8))
    
    def test_id(self):
        original = TestTransformation._generate_matrix()
        transformed = inverse_transform(transform(original))
        diff = (original - transformed).array
        self.assertAlmostEqual(np.sum(abs(diff)), 0)
    
    def test_exid(self):
        original = TestTransformation._generate_matrix()
        transformed = exinverse_transform(extransform(original))
        diff = (original - transformed).array 
        self.assertAlmostEqual(np.sum(abs(diff)), 0)


if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestMatrix),
        unittest.TestLoader().loadTestsFromTestCase(TestTransformation),
        unittest.TestLoader().loadTestsFromTestCase(TestImage),
    ])
    
    unittest.TextTestRunner(verbosity=2).run(suite)
