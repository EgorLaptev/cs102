import unittest
from src.lab1.calculator import calculator

class CalculatorTestCase(unittest.TestCase):
        
    def test_mult(self):
        self.assertEqual(calculator("3*4"), 12)    
        
    def test_div(self):
        self.assertEqual(calculator("56/2"), 28)
        
    def test_pow(self):
        self.assertEqual(calculator("5**3"), 125)
        
    def test_float(self):
        self.assertEqual(calculator("11.1*6"), 66.6)
        
    def test_div_by_zero(self):
        self.assertEqual(calculator("89/0"), 'You can not divide by zero')
        
    def test_string_input(self):
        self.assertEqual(calculator("hello, world"), 'You used forbidden symbols')
        
    def test_equal_in_string(self):
        self.assertEqual(calculator("5=4"), 'You used forbidden symbols')
        
    def test_wrong_expression(self):
        self.assertEqual(calculator("6..3 * 4"), 'Please enter the correct expression')
        
