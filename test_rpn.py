import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    
    def test_exponential(self):
        result = rpn.calculate("4 2 ^")
        self.assertEqual(16, result)

    def test_badinput(self):
        with self.assertRaises(TypeError):
            rpn.calculate("1 2 3 +")
