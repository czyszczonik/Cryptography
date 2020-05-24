import random

from AES_utils import AES_util
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from key_util import getDefaultKey
from Crypto.Util.Padding import pad, unpad

xor = lambda bytes1, bytes2:(bytes([bit1 ^ bit2 for bit1, bit2 in zip(bytes1,bytes2)]))

splitBlocks = lambda ciphertext: [ciphertext[i:i + AES.block_size]
                    for i in range(0, len(ciphertext), AES.block_size)]

zipBlocks = lambda blocks, iv: [(block, iv)
                for block, iv in zip(splitBlocks(blocks), [iv]+splitBlocks(blocks))]

def prepareBlocks(blocks):
    plaintext = b''
    for block in blocks:
        plaintext += block
    return unpad(plaintext, AES.block_size).decode()

def attack(cipthertext, iv):
    aes = AES_util()
    blocks = zipBlocks(cipthertext, iv)
    resolvedBlocks = []
    for (block, iv) in blocks:
        decrypted = bytearray(AES.block_size)
        testIV = bytearray(AES.block_size)
        for i in reversed(range(16)):
            for j in reversed(range(i, 16)):
                testIV[j] = decrypted[j] ^ AES.block_size-i
            for b in range(0, 256):
                testIV[i] = b
                ans = aes.paddingOracle(block, testIV)
                if ans:
                    decrypted[i] = testIV[i] ^ AES.block_size-i
                    break
        resolvedBlocks.append(xor(iv, decrypted))

    result = prepareBlocks(resolvedBlocks)


    print(f'Padding Oracle attack result: {result}')

if __name__ == "__main__":
    message = "My secret message"
    aes = AES_util()
    ciphertext, iv = aes.encrytption(message)
    attack(ciphertext, iv)
