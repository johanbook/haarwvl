# -*- coding: utf-8 -*-
#####################################################
# Test.py
# Johan Book
# johanbook@hotmail.com
# 2018-05-07
#
# Methods to probe the performance of the rest of
# the package.
# Methods:
# - test_matrix() : tests the matrix class
# - test_image()  : tests the image class 
# If this module is run as a script both of these
# methods will be callled.
#####################################################

import numpy as np

# Test matrix class
def test_matrix(echo=False, dim=17, tol=1e-10):
  """
  A function to evaluate the performance of the Matrix class.
  Parameters
  ----------
  echo : boolean
      whether to write to stdout or not. Use True for debugging. Default False.
  dim : int
      dimension of used test matrix.
  tol : double
      tolerance 
  Returns
  -------
  boolean
      result of the test. True for sucessful and false otherwise
  """
  
  
  # Check inverse method
  a = Matrix( np.random.rand(dim,dim) )
  i = a*a.inverse()
  b = sum( sum( abs(i.array - np.eye(dim)) ) )    
  
  # If echo is enabled print results
  if echo:
      print('='*75)
      print("Original matrix")
      print(a)
      print('='*75)
      print("Matrix times its inverse")
      print(i)
      print('='*75)
      print("Absolute sum:", b)
  
  return b <= tol

# Test image class
def test_image(path, path_compressed=None, path_uncompressed=None, echo=False, num=4):
  """
  A function to evaluate the performance of the Matrix class.
  Parameters
  ----------
  echo : boolean
      whether to write to stdout or not. Use True for debugging. Default False.
  Returns
  -------
  boolean
      result of the test
  """
  
  # Load image
  image = Image(path)
  image.display()
  b = np.array( image.matrix.array )
  
  # Compress
  image.compress(num)
  image.display()
  if not path_compressed == None:
    image.save(path_compressed)

  # Uncompress
  image.uncompress(num)
  image.display()
  if not path_uncompressed == None:
    image.save(path_uncompressed)
  c = np.array( image.matrix.array )
  
  # Estimate error
  err = abs(b-c)
  err = sum(err)/len(err)
    
  if echo:
      print("Error", err, "per pixel")
  
  return True

# Test matrix
test_matrix(echo=True)

# Test image
test_image(echo=True,
  path                = 'C:/Users/nat13jbo/Desktop/kvinna2.jpg',
  path_compressed     = 'C:/Users/nat13jbo/Desktop/compressed.jpg',
  path_uncompressed   = 'C:/Users/nat13jbo/Desktop/uncompressed.jpg',
)
