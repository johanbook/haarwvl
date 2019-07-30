"""
Johan Book
johanbook@hotmail.com
2018-05-07
"""
from nose.tools import assert_raises, assert_less_equal
import numpy as np
import os

from haarwvl.image import Image


class TestImage:
    def setup(self):
        self.image = Image(np.eye(12))

    def test_badinput(self):
        assert_raises(Exception, Image, None)

    def test_compression(self):
        b = self.image.array
        image = self.image.clone()
        image.compress(4)
        image.uncompress(4)
        c = np.array(image.array)

        # Estimate MAE error
        err = np.abs(b - c)
        err = np.sum(err) / len(err)

        # The error can be large even though the image is fine
        assert_less_equal(err, 1.0e3)

    def test_save(self):
        test_path = "test.png"
        try:
            self.image.save(test_path)
        except Exception:
            assert False

        if os.path.exists(test_path):
            os.remove(test_path)
        else:
            assert False
