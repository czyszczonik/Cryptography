import unittest
from AES_util  import AES_util
from Exercise1 import _decryptionOracle
from key_util import getDefaultKey
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util import Counter

class TestAdd(unittest.TestCase):


    def test_CBC(self):
        aes = AES_util()
        mode = "CBC"
        key = getDefaultKey()
        message = get_random_bytes(AES.block_size)
        cipher, iv = aes.encrypt(message, mode, key)
        decrypted = aes.decrypt(cipher, mode, key, iv)
        self.assertEqual(message, decrypted)
        self.assertNotEqual(message, cipher)


    def test_CFB(self):
        aes = AES_util()
        mode = "CFB"
        key = getDefaultKey()
        message = get_random_bytes(AES.block_size)
        cipher, iv = aes.encrypt(message, mode, key)
        decrypted = aes.decrypt(cipher, mode, key, iv)
        self.assertEqual(message, decrypted)
        self.assertNotEqual(message, cipher)


    def test_OFB(self):
        aes = AES_util()
        mode = "OFB"
        key = getDefaultKey()
        message = get_random_bytes(AES.block_size)
        cipher, iv = aes.encrypt(message, mode, key)
        decrypted = aes.decrypt(cipher, mode, key, iv)
        self.assertEqual(message, decrypted)
        self.assertNotEqual(message, cipher)


    def test_CTR(self):
        aes = AES_util()
        mode = "CTR"
        key = getDefaultKey()
        message = get_random_bytes(AES.block_size)
        cipher, iv = aes.encrypt(message, mode, key)
        decrypted = aes.decrypt(cipher, mode, key, iv)
        self.assertEqual(message, decrypted)
        self.assertNotEqual(message, cipher)


    def test_EAX(self):
        aes = AES_util()
        mode = "EAX"
        key = getDefaultKey()
        message = get_random_bytes(AES.block_size)
        cipher, iv = aes.encrypt(message, mode, key)
        decrypted = aes.decrypt(cipher, mode, key, iv)
        self.assertEqual(message, decrypted)
        self.assertNotEqual(message, cipher)



if __name__ == '__main__':
    unittest.main()
