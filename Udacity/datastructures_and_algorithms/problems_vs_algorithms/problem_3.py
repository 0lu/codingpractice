import heapq
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return
    if len(input_list) == 1:
        return [input_list[0], 0]
    heapq._heapify_max(input_list)
    num1 = 0
    num2 = 0
    while input_list:
        num1 = (num1 * 10) + heapq._heappop_max(input_list)
        if input_list:
            num2 = (num2 * 10) + heapq._heappop_max(input_list)
    return [num1, num2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
#Pass

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
#Pass

test_function([[1], [1, 0]])
#Pass

test_function([[1, 1, 0], [10, 1]])
#Pass

test_function([[0, 0], [0, 0]])
#Pass