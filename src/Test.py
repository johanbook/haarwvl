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

# Test matrix class
class TestMatrix(unittest.TestCase):
    def test_arithmetics(self):
        I = Matrix( np.eye(2) )
        #self.assertAlmostEqual
    
    def test_inverse(self):
        dim = 3
        a = Matrix( np.random.rand(dim,dim) )
        i = a*a.inverse() 
        q = np.sum(i.array - np.eye(dim))
  
        self.assertAlmostEqual(q,0)
        
    def test_transpose(self):
        pass

# Test image class
class TestImage(unittest.TestCase):
    def setup(self):
        import os    
    
    def test_badinput(self):
      self.assertRaises(Exception, Image, None)
    
    @unittest.skipIf(not os.path.exists(path), 'Test file does not exist: '+path)
    def test_compression(self):
      # Load image
      image = Image(path)
      b = np.array( image.matrix.array )
      
      # Compress and Uncompress
      image.compress(num)
      image.uncompress(num)
      c = np.array( image.matrix.array )
  
      # Estimate MAE error
      err = abs(b-c)
      err = sum(err)/len(err)
      
      # The error can be large even though the image is fine
      self.assertLessEqual(err, 1.e+3)
      
    @unittest.skipIf(not os.path.exists(path), 'Test file does not exist: '+path)  
    def test_save(self):
      image = Image(path)
      image.save('test')
      
 # Transformation class     
class TestTransformation(unittest.TestCase):
    def _generate_matrix():
        return Matrix( np.random.rand(8,8) )
    
    def test_id(self):
        original = TransformationTest._generate_matrix()
        transformed = inverse_transform( transform(original) )
        diff = (original - transformed).array
        self.assertAlmostEqual(np.sum(abs(diff)), 0)
    
    def test_exid(self):
        original = TransformationTest._generate_matrix()
        transformed = exinverse_transform( extransform(original) )
        diff = (original - transformed).array 
        self.assertAlmostEqual(np.sum(abs(diff)), 0)

if __name__=='__main__':
    path                = 'C:/Users/nat13jbo/Desktop/kvinna2.jpg'
    
    matrixTest = unittest.TestLoader().loadTestsFromTestCase(TestMatrix)
    transformationTest = unittest.TestLoader().loadTestsFromTestCase(TestTransformation)
    imageTest = unittest.TestLoader().loadTestsFromTestCase(TestImage)
    suite = unittest.TestSuite( [matrixTest, transformationTest, imageTest] )
    
    unittest.TextTestRunner(verbosity=2).run(suite)
