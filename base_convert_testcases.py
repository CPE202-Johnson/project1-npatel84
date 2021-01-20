import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        pass

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        pass

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
        pass

if __name__ == "__main__":
        unittest.main()

          