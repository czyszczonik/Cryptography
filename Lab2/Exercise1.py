import random

from AES_util import AES_util
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from InitialGenerator import InitialGenerator
from cli_utils import *

def challenge(inputs, key, mode="CBC", init = None):
    if len(inputs) != 2:
        print(f"Expected 2 messages but received [{len(inputs)}]")
        exit()
    bit = random.SystemRandom().randint(0,1)
    aes = AES_util()
    return aes.encrypt(inputs[bit], mode, key, init)[0]

def encryptionOracle(inputs, key,  mode="CBC", init = None):
    encrypted = []
    aes = AES_util()
    for message in inputs:
        encrypted.append(aes.encrypt(message, mode, key, init))
    return _only_ciphertext(encrypted)

def _only_ciphertext(ciphertexts):
    msg = []
    for tuple in ciphertexts:
        msg.append(tuple[0])
    return msg
if __name__ == "__main__":
    args, mode = get_args()
    key = get_key(args)
    if mode:
        messages = get_files(args)
    else:
        messages = get_messages(args)

    if args.challenge:
        result = challenge(messages, key, args.mode)
    else:
        result = encryptionOracle(messages, key, args.mode)

    print(result)


# EXCENDED FUNCTIONALITY
def _encryptionOracle_unsecure(inputs, key,  generator,  mode="CBC", init = None):
    encrypted = []
    aes = AES_util(generator)
    for message in inputs:
        encrypted.append(aes.encrypt(message, mode, key, init))
    return encrypted

def _challenge_unsecure(inputs, key, initGen, mode="CBC", init = None):
    if len(inputs) != 2:
        print(f"Expected 2 messages but received [{len(inputs)}]")
        exit()
    bit = random.SystemRandom().randint(0,1)
    aes = AES_util(initGen)
    if init is None:
        return aes.encrypt(inputs[bit], mode, key), bit
    else:
        return aes.encrypt(inputs[bit], mode, key), bit

def _decryptionOracle(inputs, key,  mode="CBC"):
    decrypted = []
    aes = AES_util()
    for tuple in inputs:
        decrypted.append(aes.decrypt(tuple[0], mode, key, tuple[1]))
    return decrypted

def _only_ciphertext(ciphertexts):
    msg = []
    for tuple in ciphertexts:
        msg.append(tuple[0])
    return msg
