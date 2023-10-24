import unittest

from src.lab2.rsa import is_prime, gcd, multiplicative_inverse

class TestVignere(unittest.TestCase):
    
    def setUp(self):
        self.is_prime = is_prime
        self.gcd = gcd
        self.multiplicative_inverse = multiplicative_inverse

    def test_is_prime(self):
        self.assertEqual(is_prime(0), True)
        self.assertEqual(is_prime(13), True)
        self.assertEqual(is_prime(1), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(65), False)
        self.assertEqual(is_prime(-12), False)

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)
        self.assertEqual(gcd(43, 1), 1)
        self.assertEqual(gcd(0, 1), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(34, 1), 0)
        self.assertEqual(multiplicative_inverse(234, 23423), 6106)

