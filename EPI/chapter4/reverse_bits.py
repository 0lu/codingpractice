

def swap_bit(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


def reverse_bits1(x: int) -> int:
    for i, j in zip(range(63, 31, -1), range(0, 32)):
        x = swap_bit(x, i, j)
    return x


def reverse_bits_1(x: int) -> int:
    for i, j in zip(range(15, 7, -1), range(0, 8)):
        x = swap_bit(x, i, j)
    return x


cache = [reverse_bits_1(x) for x in range(2 ** 16)]


def reverse_bits(x: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    return (cache[(x >> (3 * mask_size)) & bit_mask]
            | cache[(x >> (2 * mask_size)) & bit_mask] << mask_size
            | cache[(x >> mask_size) & bit_mask] << (mask_size * 2)
            | cache[x & bit_mask] << (mask_size * 3))
