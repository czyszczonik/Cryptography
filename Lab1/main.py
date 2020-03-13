from random import randint

from Lab1.adversary import predict_glibc_random
from Lab1.adversary import predict_lcg
from Lab1.glibc import random
from Lab1.lcg_generator import lcg


def create_lcg(init_size, test_size):
    modulo = 2 ** 31
    multiplier = 123
    increment = 12345
    seed = randint(1, modulo)
    return lcg(modulo, multiplier, increment, seed, init_size, test_size)


def create_random(test_size, init_size):
    seed = randint(1, 2 ** 31)
    return random(seed, test_size, init_size)


def test(init_size, test_size, generator, adversary, name):
    # Generate initial values for adversary
    initial_values = []
    for _ in range(init_size):
        initial_values.append(next(generator))

    correct, incorrect = 0, 0
    previous = initial_values

    for generated_value in generator:
        predicted = adversary(previous)
        if predicted == generated_value:
            correct += 1
        previous.append(generated_value)

    print("Attack on " + name)
    print("Numbers to predict: " + str(test_size))
    print("Number of initial values: " + str(init_size))
    print('Positive predicted numbers: ' + str(correct * 100 / test_size) + "%")


def lcg_test():
    test_size = 10000
    init_size_lcg = 12
    generator = create_lcg(init_size_lcg, test_size)
    test(init_size_lcg, test_size, generator, predict_lcg, "LCG")


def glibc_test():
    test_size = 10000
    init_size_glibc = 32
    generator = create_random(init_size_glibc, test_size)
    test(init_size_glibc, test_size, generator, predict_glibc_random, "glibc random()")


if __name__ == "__main__":
    print()
    lcg_test()
    print()
    glibc_test()
