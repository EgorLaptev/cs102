import unittest

from src.lab2.vigenre import decrypt_vigenere, encrypt_vigenere

class TestVignere(unittest.TestCase):
    
    def setUp(self):
        self.decrypt_vigenere = decrypt_vigenere
        self.encrypt_vigenere = encrypt_vigenere

    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere('ATTACKATDAWN', 'LEMON'), 'LXFOPVEFRNHR')
        self.assertEqual(encrypt_vigenere('HELL', 'HELL'), 'OIWW')
        self.assertEqual(encrypt_vigenere('WTF', ''), 'WTF')
        self.assertEqual(encrypt_vigenere('DUCK', 'UKVB'), 'XEXL')
        self.assertEqual(encrypt_vigenere('', 'UKVB'), '')
    
    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere('PYTHON', 'A'), 'PYTHON')
        self.assertEqual(decrypt_vigenere('LXFOPVEFRNHR', 'LEMON'), 'ATTACKATDAWN')
        self.assertEqual(decrypt_vigenere('LXFOPVEFRNHR', ''), 'LXFOPVEFRNHR')
        self.assertEqual(decrypt_vigenere('GARDEN', 'FJEIFK3FKFJSIOEL'), 'BRNVZD')
        self.assertEqual(decrypt_vigenere('GARDEN', '$$*JG/A'), 'PJUUYL')

    