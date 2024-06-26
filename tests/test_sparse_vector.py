import numpy as np
from pgvector.utils import SparseVector
import pytest


class TestSparseVector:
    def test_from_dense(self):
        assert SparseVector.from_dense([1, 2, 3]).to_list() == [1, 2, 3]
        assert SparseVector.from_dense([1, 2, 3]).to_numpy().tolist() == [1, 2, 3]

    def test_repr(self):
        assert repr(SparseVector.from_dense([1, 2, 3])) == 'SparseVector(3, [0, 1, 2], [1.0, 2.0, 3.0])'
        assert str(SparseVector.from_dense([1, 2, 3])) == 'SparseVector(3, [0, 1, 2], [1.0, 2.0, 3.0])'

    def test_dim(self):
        assert SparseVector.from_dense([1, 2, 3]).dim() == 3
