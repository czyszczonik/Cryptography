from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from InitialGenerator import InitialGenerator
from Crypto.Util import Counter
from key_util import getDefaultKey

class AES_util():
    def __init__(self, init = None):
        if init is None:
            self.init = InitialGenerator()
        else:
            self.init = init
        self.key = getDefaultKey()

    def padding(self, message):
        if type(message) is str:
            message = message.encode()
        return pad(message, AES.block_size)

    def encrytption(self, message):
        aes = AES_util()
        message = self.padding(message)
        return aes.encrypt(message, self.key)

    def encrypt(self, message, key):
        cipher = self._getCipher(key)
        return cipher.encrypt(message), self.init.getPrevious()

    def _getCipher(self, key):
        init = self.init.getIV()
        return AES.new(key, AES.MODE_CBC, init)

    def paddingOracle(self, ciphertext, iv):
        cipher = AES.new(key=self.key, mode=AES.MODE_CBC, iv=iv)
        message = cipher.decrypt(ciphertext)
        try:
            unpad(message, AES.block_size)
            return True
        except ValueError:
            return False
