
def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = 1 << i | 1 << j
        x ^= bit_mask
    return x


print(swap_bits(37, 2, 3))
