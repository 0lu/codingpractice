
def count_bits(x):
    breakpoint()
    bits = 0
    while x:
        bits += x & 1
        x >>= 1
    return bits


print(count_bits(255))