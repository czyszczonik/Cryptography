import random

from AES_util import AES_util
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrytption(inputs, key,  mode="CBC"):
    aes = AES_util()
    return aes.encrypt(message, mode, key, init)

if __name__ == "__main__":
    message = get_random_bytes(AES.block_size - 1)
    result = encrytption(messages, key, args.mode)
