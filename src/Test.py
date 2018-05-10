# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:35:33 2018

@author: bas12ban
"""

########################################
# Test.py
# Johan Book
# 2018-05-07
########################################

import Imageclass

# Variables
path                = 'C:/Users/bas12ban/Desktop/stuff.png'
path_compressed     = 'C:/Users/bas12ban/Desktop/compressed.jpg'
path_uncompressed   = 'C:/Users/bas12ban/Desktop/uncompressed.jpg'
num                 = 4

# Load image
image = Image(path)
image.display()

# Compress
image.compress(num)
image.display()
image.save(path_compressed)

# Uncompress
image.uncompress(num)
image.display()
image.save(path_uncompressed)
