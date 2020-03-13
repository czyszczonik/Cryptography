import random


def lcg(modulus, a, c, seed=random.randint(0, 1000000), init_size=9, test_size=10000):
    generated = 0
    while generated < test_size + init_size:
        seed = (a * seed + c) % modulus
        generated += 1
        yield seed
