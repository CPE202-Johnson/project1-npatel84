import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        
    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        
    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
    
    def test_base11(self):
        self.assertEqual(convert(21,11),"1A")
    
    def test_base12(self):
        self.assertEqual(convert(23,12),"1B")
    
    def test_base13(self):
        self.assertEqual(convert(25,13),"1C")
    
    def test_base14(self):
        self.assertEqual(convert(27,14),"1D")
    
    def test_base15(self):
        self.assertEqual(convert(29,15),"1E")
    
    def test_base16(self):
        self.assertEqual(convert(31,16),"1F")
    

        

if __name__ == "__main__":
        unittest.main()

          