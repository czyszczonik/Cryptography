def random(seed, test_size, init_size):
    int32 = lambda x: x & 0xffffffff - 0x100000000 if x & 0xffffffff > 0x7fffffff else x & 0xffffffff
    int64 = lambda \
            x: x & 0xffffffffffffffff - 0x10000000000000000 if x & 0xffffffffffffffff > 0x7fffffffffffffff else x & 0xffffffffffffffff

    r = [0] * 344
    r[0] = seed

    for i in range(1, 31):
        r[i] = int32(int64(16807 * r[i - 1]) % 0x7fffffff)

        if r[i] < 0:
            r[i] = int32(r[i] + 0x7fffffff)

    for i in range(31, 34):
        r[i] = int32(r[i - 31])

    for i in range(34, 344):
        r[i] = int32(r[i - 31] + r[i - 3])

    i = 344 - 1

    generated = 0
    while generated < test_size + init_size:
        i += 1
        generated += 1
        r.append(int32(r[i - 31] + r[i - 3]))
        yield int32((r[i] & 0xffffffff) >> 1)
