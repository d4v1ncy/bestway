from bestway import fromstr, xor, Exit
from unittest import TestCase


def equal(lhs, rhs):
    assert lhs == rhs, f'{lhs} != {rhs}'
    return True


class TestBestWay(TestCase):
    def test_fromstr(self):
        assert equal(fromstr('ABBA'), 5)
        assert equal(fromstr('EMMA'), 4)
        assert equal(fromstr('AMA'), 77)
        assert equal(fromstr('OMO'), 77)
        assert equal(fromstr('BABA'), 5)
        assert equal(fromstr('DOOR'), 22)
        assert equal(fromstr('WINDOW'), 12)
        assert equal(fromstr('ERROR'), 88)
        assert equal(fromstr('FAILURE'), 64)

    def test_xor(self):
        assert equal(xor(0b10, 0b01), 0b11)
        assert equal(xor(0b100, 0b001), 0b101)
        assert equal(xor(0b1000, 0b0001), 0b1001)
        assert equal(xor(ord('*'), ord('%')), 15)

    def test_exit(self):
        assert isinstance(Exit('TEST'), SystemExit)
        assert hasattr(Exit('TEST'), 'code')
        assert equal(Exit('TEST').code, 22)
