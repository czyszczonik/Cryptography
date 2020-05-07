import random
import time

from key_util import getDefaultKey
from Exercise1 import _challenge_unsecure, _encryptionOracle_unsecure
from Crypto.Cipher import AES
from InitialGenerator import InitialGenerator
from Crypto.Random import get_random_bytes
from sys import byteorder


def CPAExperiment(total):
    start = time.time()

    generator = InitialGenerator(True)
    key = getDefaultKey()
    baseMessage = get_random_bytes(AES.block_size)

    baseCipher, baseIV = _encryptionOracle_unsecure([baseMessage], key, generator)[0]
    win = 0
    iv = baseIV

    for i in range(total):
        nextIV = compute_next_IV(iv)
        prepared = prepare_message(baseMessage, baseIV, nextIV)
        random = get_random_bytes(AES.block_size)
        while random is prepared:
            random = get_random_bytes(AES.block_size)

        output, bit = _challenge_unsecure([prepared, random], key, generator)
        cipher, iv = output[0], output[1]
        guessed = guess_bit(baseCipher,cipher)
        if guessed == bit:
            win += 1

    end = time.time()
    print(f"Guessed [{win}] of [{total}] attempts [{win*100/total}%].")
    print(f"Guessed in [{end - start} s]")
    print(f"Average time [{(end - start)/total} s]")

prepare_message = lambda bytes1, bytes2, bytes3: (xor(bytes3, xor(bytes2, bytes1)))
xor = lambda bytes1, bytes2:(bytes([bit1 ^ bit2 for bit1, bit2 in zip(bytes1,bytes2)]))
guess_bit = lambda a, b: 0 if (a == b) else 1
compute_next_IV = lambda iv: (int(iv.hex(), 16) + 1).to_bytes(AES.block_size, 'big')

CPAExperiment(100000)
