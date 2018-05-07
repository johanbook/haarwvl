**Warning:** Prepare for Johan's pseudo code! Also note, this should be the public methods you use. 
Feel free to add any private methods in your code. 

# Matrix (David)
Makes it easier to manipulate matrices, keeps the rest of the code clean and tidy :)

**def init(array)** 
<br>&nbsp;&nbsp;&nbsp;&nbsp;
takes an array and stores it
<br>
**def add()**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
add matrices
<br>
**def sub()**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
subbtracts matrices
<br>
**def mul()**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
multiplication
<br>
**def pow()**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
power
<br>
**def inverse()**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
inverse (use np.linalg?)
<br>
**def transpose()**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
transposes matrix
<br>
**def rep()**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
creates string representation of matrix

# Transform (not a class) (Frank)
does the transformation (and inverse) of given matrix. Nice of one can determine the weigth used in the matrix. 
Perhaps a mode of whether Matrix.transpose() or Matrix.inverse() is to be used?

**def transform(Matrix)** 
<br>&nbsp;&nbsp;&nbsp;&nbsp;
performs transformation on matrix
<br>
**def inverse_transform(Matrix)** 
<br>&nbsp;&nbsp;&nbsp;&nbsp;
performs inverse transformation on matrix

# Image (Björn)
Contains an image and appropriate methods for handling it.

**def init(String path)** 
<br>&nbsp;&nbsp;&nbsp;&nbsp;
Creates an image from a string, throws appropriate erros. Cuts rows/columns to get even number
<br>
**def save(String path)**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
save this image to a given path. Throws appropriate errors
<br>
**def compress(num=1)**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
compress image *num* times.
<br>
**def uncompress(num=1)**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
compress image *num* times.
<br>
**def display()**
<br>&nbsp;&nbsp;&nbsp;&nbsp;
displays the image (use matplotlib plot?)

# Test (Johan)
Some code that loads an image, displays it, compressses it, displays and saves it, uncompresses, displays and saves it
