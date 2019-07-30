"""
Johan Book
johanbook@hotmail.com
2018-05-07
"""
from nose.tools import assert_almost_equal
import numpy as np

from haarwvl.transform import (
    transform,
    inverse_transform,
    exinverse_transform,
    extransform,
)


class TestTransform:
    def _transform(self, transform, inverse):
        original = np.eye(12)
        transformed = inverse(transform(original))
        diff = original - transformed
        assert_almost_equal(np.sum(abs(diff)), 0)

    def test_implicit_transform(self):
        self._transform(transform, inverse_transform)

    def test_explicit_transform(self):
        self._transform(extransform, exinverse_transform)
