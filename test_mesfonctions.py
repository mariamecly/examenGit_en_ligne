import unittest
from mesfonctions import add, sub, mul, div, square

class TestMath(unittest.TestCase):
    def test_add(self): 
        self.assertEqual(add(1, 2), 3)
    def test_sub(self): 
        self.assertEqual(sub(5, 2), 3)
    def test_mul(self): 
        self.assertEqual(mul(3, 3), 9)
    def test_div(self): 
        self.assertEqual(div(10, 2), 5)
    def test_square(self): 
        self.assertEqual(square(4), 16)

if __name__ == '__main__':
    unittest.main()