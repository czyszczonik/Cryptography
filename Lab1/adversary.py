from functools import reduce
from math import gcd
from Lab1.math_tools import mod_inv


def predict_lcg(generated_values, previous_visibility=12):
    modulo = _compute_modulo(generated_values, previous_visibility)
    multiplier = _compute_multiplier(generated_values, modulo)
    increment = _compute_increment(generated_values, multiplier, modulo)
    return (multiplier * generated_values[-1] + increment) % modulo


# This function compute modulo from simple equation
# t2*t0 - t1*t1 = (m*m*t0 * t0) - (m*t0 * m*t0) = 0 (mod n)
# This can be resolved from recurrent formula T(n) = S(n+1) - S(n)
# t0 = s1 - s0
# t1 = s2 - s1 = (s1*m + c) - (s0*m + c) = m*(s1 - s0) = m*t0 (mod n)
# t2 = s3 - s2 = (s2*m + c) - (s1*m + c) = m*(s2 - s1) = m*t1 (mod n)
# and using chinese remainder theorem we compute modulo.

def predict_glibc_random(generated_values):
    if len(generated_values) < 32:
        raise ValueError("You fucked up! you must deliver at least 32 generated values.")
    return (generated_values[-31] + generated_values[-3]) % (2 ** 31)


def _compute_modulo(generated_values, previous_visibility):
    last_index = min(previous_visibility, len(generated_values))
    n_1 = last_index - 1

    differences = [element_1 - element_0 for element_1, element_0 in
                   zip(generated_values[-1 * n_1:], generated_values[-1 * last_index:-1])]

    # t2*t0 - t1*t1 = (m*m*t0 * t0) - (m*t0 * m*t0) = 0 (mod n)
    zeros = [diff_2 * diff_0 - diff_1 * diff_1 for diff_0, diff_1, diff_2 in
             zip(differences, differences[1:], differences[2:])]

    # chinese remainder theorem
    return abs(reduce(gcd, zeros))


def _compute_multiplier(values, modulo):
    try:
        # multiplier = (value_2 - value_1)/(value_1 - value_0)  (mod n)
        return (values[-1] - values[-2]) * mod_inv((values[-2] - values[-3]), modulo) % modulo
    except ValueError:
        return 0  # mod_inv cannot find inverse in specific field


def _compute_increment(values, multiplier, modulo):
    return (values[-1] - (values[-2] * multiplier)) % modulo
