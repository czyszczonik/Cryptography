from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from InitialGenerator import InitialGenerator
from Crypto.Util import Counter

BS = 16
pad5 = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad5 = lambda s : s[0:-ord(s[-1])]

class AES_util():
    def __init__(self, init = None):
        if init is None:
            self.init = InitialGenerator()
        else:
            self.init = init


    def encrypt(self, message, mode, key, init = None):
        mode = self._mode(mode)
        cipher = self._getCipher(mode, key, init)
        message = self._prepare_message(message, mode)
        return cipher.encrypt(message), self.init.getPrevious()


    def decrypt(self, ciphertext, mode, key, init = None):
        mode =  self._mode(mode)
        cipher = self._getCipher(mode, key, init)
        ciphertext = self._prepare_ciphertext(ciphertext, mode)
        text = cipher.decrypt(ciphertext)
        return self._process_message(text, mode)


    def _prepare_message(self, message, mode):
        if type(message) is str:
            message = message.encode()
        if mode is AES.MODE_CBC:
            message = pad(message, AES.block_size, style='pkcs7')
            m2 = pad5(message)
            if message == m2:
                print("DUPA")
        return message


    def _prepare_ciphertext(self, ciphertext, mode):
        if type(ciphertext) is str:
            ciphertext = ciphertext.encode()
        return ciphertext


    def _process_message(self, message, mode):
        if mode is AES.MODE_CBC:
            message = unpad(message, AES.block_size, style='pkcs7')
        return message


    def _getCipher(self, mode, key, init):
        if mode in [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]:
            if init is None:
                init = self.init.getIV()
            return AES.new(key, mode, init)
        elif mode in [AES.MODE_EAX]:
            if init is None:
                init = self.init.getNonce()
            return AES.new(key, mode, init)
        elif mode in [AES.MODE_CTR]:
            if init is None:
                init = self.init.getNonce()
            counter = Counter.new(128, initial_value=int(init.hex(),16))
            return AES.new(key, mode, counter = counter)
        else:
            raise Exception(f"Can't resolve: [{mode}].")


    def _mode(self, mode):
        mode = mode.upper()
        encryptionModes = {
            'CBC' : AES.MODE_CBC,
            'CFB' : AES.MODE_CFB,
            'OFB' : AES.MODE_OFB,
            'CTR' : AES.MODE_CTR,
            'EAX' : AES.MODE_EAX
        }
        return encryptionModes[mode]
