
def count_bits(x):
    bits = 0
    while x:
        bits += x & 1
        x >>= 1
    return bits

