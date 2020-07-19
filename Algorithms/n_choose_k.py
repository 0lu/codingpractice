import copy


def perm_with_repetitions(arr, num):
    def perm_helper(arr, index, num, curr, result):
        if num == 0:
            result.append(copy.deepcopy(curr))
            return

        for i in range(len(arr)):
            curr.append(arr[i])
            perm_helper(arr, i, num - 1, curr, result)
            curr.pop()

    result = []
    perm_helper(arr, 0, num, [], result)
    return result


def perm_with_repetitions_2(arr, num):
    def perm_helper(arr, index, num, curr):
        if num == 0:
            return copy.deepcopy(curr)

        results = []
        for i in range(len(arr)):
            curr.append(arr[i])
            results.append(perm_helper(arr, i, num - 1, curr))
            curr.pop()

        return results

    return perm_helper(arr, 0, num, [])


def perm_without_repetitions(arr, num):
    def perm_helper(arr, index, num, map, curr, result):
        if num == 0:
            result.append(copy.deepcopy(curr))
            return

        for i in range(len(arr)):
            if not map[i]:
                curr.append(arr[i])
                map[i] = True
                perm_helper(arr, i, num - 1, map, curr, result)
                curr.pop()
                map[i] = False

    map = [False for _ in arr]
    result = []
    perm_helper(arr, 0, num, map, [], result)
    return result

def perm_without_repetitions_2(arr, num):
    def perm_helper(arr, index, num, map, curr, result):
        if num == 0:
            return copy.deepcopy(curr)

        result = []
        for i in range(len(arr)):
            if not map[i]:
                curr.append(arr[i])
                map[i] = True
                result.append(perm_helper(arr, i, num - 1, map, curr, result))
                curr.pop()
                map[i] = False
        return result

    map = [False for _ in arr]
    result = []
    return perm_helper(arr, 0, num, map, [], result)

def combinations_with_repetitions(arr, num):
    def combination_helper(arr, index, num, curr, result):
        if num == 0:
            result.append(copy.deepcopy(curr))
            return

        for i in range(index, len(arr)):
            curr.append(arr[i])
            combination_helper(arr, i, num - 1, curr, result)
            curr.pop()

    result = []
    combination_helper(arr, 0, num, [], result)
    return result

def combinations_without_repetitions(arr, num):
    def combination_helper(arr, index, num, curr, result):
        if num == 0:
            result.append(copy.deepcopy(curr))
            return

        for i in range(index + 1, len(arr)):
            curr.append(arr[i])
            combination_helper(arr, i, num - 1, curr, result)
            curr.pop()

    result = []
    combination_helper(arr, -1, num, [], result)
    return result


print(perm_with_repetitions(["a", "b", "c"], 2))
print(perm_with_repetitions_2(["a", "b", "c"], 2))
print(perm_without_repetitions(["a", "b", "c"], 2))
print(perm_without_repetitions_2(["a", "b", "c"], 2))
print(combinations_with_repetitions(["a", "b", "c"], 2))
print(combinations_without_repetitions(["a", "b", "c"], 2))




