
def parity1(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def parity2(x):
    result = 0
    while x:
        result += x & 1
        x >>= 1
    return result % 2

def parity3(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


cache = {i: parity1(i) for i in range(2**16)}


def parity4(x):
    bitmask = 0xFFFF
    return cache[x >> 3 * 16] \
        ^ cache[(x >> 2 * 16) & bitmask] \
        ^ cache[(x >> 16) & bitmask] \
        ^ cache[x & bitmask]


def parity5(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


print(parity1(4))
print(parity1(3))

print(parity2(4))
print(parity2(3))

print(parity3(4))
print(parity3(3))

print(parity4(4))
print(parity4(3))

print(parity5(4))
print(parity5(3))