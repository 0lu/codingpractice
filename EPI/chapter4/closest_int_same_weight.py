from EPI.chapter4.count_bits import count_bits
import sys

def closest_int_same_bit_count_brute_force(x: int) -> int:
    # TODO - you fill in here
    bits = count_bits(x)
    left, right = 0, 0
    for i in range(x - 1, 0, -1):
        if count_bits(i) == bits:
            left = i
            break
    for i in range(x+1, sys.maxsize):
        if count_bits(i) == bits:
            right = i
            break
    print(left)
    return left if abs(left - x) < abs(right - x) else right

print(closest_int_same_bit_count_brute_force(1))
