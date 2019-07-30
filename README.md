2018-05-07
# haarwvl
**Björn Annby, Johan Book, Frank Johansson and David Linehan**

A project done in the course NUMA01 on image compression using Haar wavelets.

#### Install
The package can be installed using `pipenv install`. If you do not have pipenv it can be installed using`pip install pipenv`.

#### Usage
```python
from haarwvl import Image

image = Image('image.png')
image.compress()
image.save('compressed_image.png')

```