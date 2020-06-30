def merge_lists(lst1, lst2):
    # Write your code here
    """
    i, j = 0, 0
    list3 = []

    while i < len(lst1) and j < len(lst2):
        if (lst1[i] < lst2[j]):
            list3.append(lst1[i])
            i += 1
        else:
            list3.append(lst2[j])
            j += 1

    for i in range(i, len(lst1)):
        list3.append(lst1[i])

    for j in range(j, len(lst2)):
        list3.append(lst2[j])

    return list3
    """
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            i += 1
        else:
            lst1.insert(i, lst2[j])
            i += 1
            j += 1

    while j < len(lst2):
        lst1.append(lst2[j])
        j += 1

    return lst1

lst1 = [1,3,5]
lst2 = [2,4,6,8]

merge_lists(lst1, lst2)