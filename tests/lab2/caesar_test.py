import unittest

from src.lab2.caesar import decrypt_caesar, encrypt_caesar

class TestCaesar(unittest.TestCase):
    
    def setUp(self):
        self.decrypt_caesar = decrypt_caesar
        self.encrypt_caesar = encrypt_caesar

    def test_decrypt_caesar(self):
        self.assertEqual(encrypt_caesar('Python3.6', 3), 'Sbwkrq3.6')
        self.assertEqual(encrypt_caesar('HelloWorld', 20), 'ByffiQilfx')
        self.assertEqual(encrypt_caesar('Oh', -1), 'Ng')
        self.assertEqual(encrypt_caesar('TooBig', 32), 'ZuuHom') 
        self.assertEqual(encrypt_caesar('Stay', 0), 'Stay') 
        self.assertEqual(encrypt_caesar('WTF', 23423483), 'BYK') 
        self.assertEqual(encrypt_caesar('TooLower', -234882), 'VqqNqygt') 
        self.assertEqual(encrypt_caesar('', -43), '') 

    def test_encrypt_caesar(self):
        self.assertEqual(decrypt_caesar('Sbwkrq3.6', 3), 'Python3.6')
        self.assertEqual(decrypt_caesar('GdkknVnqkc', 1), 'FcjjmUmpjb')
        self.assertEqual(decrypt_caesar('NFiejssj#2', 0), 'NFiejssj#2')
        self.assertEqual(decrypt_caesar('NFiejssj#2', 3234), 'DVyuziiz#2')
        self.assertEqual(decrypt_caesar('NFie23!^#2', -344), 'TLok23!^#2')
        self.assertEqual(decrypt_caesar('', 344), '')
