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

import Imageclass
import Matrix

import numpy as np

# Test matrix class
def test_matrix(echo=False):
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
  
  # Check inverse method
  dim = 3
  Matrix a = Matrix( np.random.rand(dim,dim) )
  Matrix a_inv = a.inverse()
  b = ( a*a.inverse() == Matrix(np.eye(dim)) )                 
  
  return True

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
  
  return True

# Test matrix
test_matrix()

# Test image
test_image(
  path                = 'C:/Users/bas12ban/Desktop/stuff.png',
  path_compressed     = 'C:/Users/bas12ban/Desktop/compressed.jpg',
  path_uncompressed   = 'C:/Users/bas12ban/Desktop/uncompressed.jpg',
)
