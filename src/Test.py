########################################
# Test.py
# Johan Book
# 2018-05-07
########################################

import Image

# Variables
path                = 'res/kvinna.jpg'
path_compresed      = 'res/compressed.jpg'
path_uncompressed   = 'res/uncompressed.jpg'
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
image.dispay()
image.save(path_uncompressed)
