import unittest
from caesar_cipher import encrypt, decrypt

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_lowercase(self):
        self.assertEqual(encrypt('abc', 3), 'def')

    def test_encrypt_uppercase(self):
        self.assertEqual(encrypt('XYZ', 3), 'ABC')

    def test_decrypt_lowercase(self):
        self.assertEqual(decrypt('def', 3), 'abc')

    def test_decrypt_uppercase(self):
        self.assertEqual(decrypt('ABC', 3), 'XYZ')

    def test_encrypt_with_nonalpha(self):
        self.assertEqual(encrypt('abc! 123', 3), 'def! 123')

    def test_decrypt_with_nonalpha(self):
        self.assertEqual(decrypt('def! 123', 3), 'abc! 123')

if __name__ == '__main__':
    unittest.main()
