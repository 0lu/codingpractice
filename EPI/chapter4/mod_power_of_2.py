
def mod_power_of_two1(x, power):
    return x & ((1 << power) - 1)


def mod_power_of_two2(x, power):
    return x ^ (1 << power)


print(mod_power_of_two1(77, 6))

print(mod_power_of_two2(77, 6))
