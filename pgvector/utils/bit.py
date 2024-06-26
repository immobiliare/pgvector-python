import numpy as np
from struct import pack, unpack_from


class Bit:
    def __init__(self, value):
        if isinstance(value, str):
            self._value = __class__.from_text(value)._value
        else:
            value = np.asarray(value, dtype=bool)

            if value.ndim != 1:
                raise ValueError('expected ndim to be 1')

            self._value = value

    def __repr__(self):
        return f'Bit({self.to_text()})'

    def to_list(self):
        return self._value.tolist()

    def to_numpy(self):
        return self._value

    def to_text(self):
        return ''.join(self._value.astype(np.uint8).astype(str))

    def to_binary(self):
        return pack('>i', len(self._value)) + np.packbits(self._value).tobytes()

    def from_text(value):
        return Bit(np.asarray([v != '0' for v in value], dtype=bool))

    def from_binary(value):
        count = unpack_from('>i', value)[0]
        buf = np.frombuffer(value, dtype=np.uint8, offset=4)
        return Bit(np.unpackbits(buf, count=count).astype(bool))

    def _to_db(value):
        if not isinstance(value, Bit):
            raise ValueError('expected bit')

        return value.to_text()

    def _to_db_binary(value):
        if not isinstance(value, Bit):
            raise ValueError('expected bit')

        return value.to_binary()
