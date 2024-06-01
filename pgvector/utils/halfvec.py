import numpy as np
from struct import pack, unpack_from


class HalfVector:
    def __init__(self, value):
        if isinstance(value, np.ndarray):
            value = value.tolist()

        if not isinstance(value, (list, tuple)):
            raise ValueError('expected list or tuple')

        self._value = value

    def to_list(self):
        return list(self._value)

    def __repr__(self):
        return f'HalfVector({self._value})'

    def to_db(value, dim=None):
        if value is None:
            return value
        if isinstance(value, HalfVector):
            value = value._value

        if dim is not None and len(value) != dim:
            raise ValueError('expected %d dimensions, not %d' % (dim, len(value)))

        return '[' + ','.join([str(float(v)) for v in value]) + ']'

    def to_db_binary(value):
        if value is None:
            return value
        if isinstance(value, HalfVector):
            value = value._value
        return pack(f'>HH{len(value)}e', len(value), 0, *value)

    def from_db(value):
        if value is None or isinstance(value, HalfVector):
            return value
        return HalfVector([float(v) for v in value[1:-1].split(',')])

    def from_db_binary(value):
        if value is None or isinstance(value, HalfVector):
            return value
        dim, unused = unpack_from('>HH', value)
        return HalfVector(unpack_from(f'>{dim}e', value, 4))
