def extended_gcd(b, n):
    x, lx = 1, 0
    y, ly = 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x, lx = lx, x - q * lx
        y, ly = ly, y - q * ly
    return b, x, y


def mod_inv(b, n):
    g, x, _ = extended_gcd(b, n)
    if g != 1:
        raise ValueError("Can't find inverse in this field!")
    return x % n
