def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not number and not isinstance(number, int):
        return
    if number <= 0:
        return 0
    if number == 1:
        return 1
    low = 0
    high = number
    prev_small = 0

    while low <= high:
        mid = low + (high - low) // 2
        remainder = number // mid
        if remainder == mid:
            return remainder
        if remainder < mid:
            high = mid - 1
        else:
            low = mid + 1
            prev_small = low

    return prev_small

print ("Pass" if  (3 == sqrt(9)) else "Fail")
#Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
#Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
#Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")
#Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
#Pass
print ("Pass" if  (None == sqrt("")) else "Fail")
#Pass
