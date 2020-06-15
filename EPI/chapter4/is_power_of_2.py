
def is_power_of_two(x):
    return x & x - 1 == 0 or x == 1


print(is_power_of_two(4))
print(is_power_of_two(67))
