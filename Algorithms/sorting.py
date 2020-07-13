
def selection_sort(array):

    def find_min(array, i):
        min = array[i]
        min_index = i
        for i in range(i, len(array)):
            if array[i] < min:
                min = array[i]
                min_index = i
        return min_index

    for i in range(len(array)):
        min_index = find_min(array, i)
        array[min_index], array[i] = array[i], array[min_index]


def insertion_sort(array):

    def insert_into(array, i, value):

        while i >= 0 and value < array[i]:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = value

    for i in range(1, len(array)):
        insert_into(array, i - 1, array[i])


def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swapped:
            break


def merge_sort(array):
    merge_sort_helper(array, 0, len(array) - 1)

def merge_sort_helper(array, l, r):

    def merge(array, l, m, r):
        ls = m - l + 1
        rs = r - m
        ls = [array[l + i] for i in range(ls)]
        rs = [array[m + 1 + i] for i in range(rs)]

        i = j = 0
        k = l
        while i < len(ls) and j < len(rs):
            if ls[i] < rs[j]:
                array[k] = ls[i]
                i += 1
            else:
                array[k] = rs[j]
                j += 1
            k += 1
        while i < len(ls):
            array[k] = ls[i]
            i += 1
            k += 1
        while j < len(rs):
            array[k] = rs[j]
            j += 1
            k += 1

    if l >= r:
        return

    m = l + (r - l)//2
    merge_sort_helper(array, l, m)
    merge_sort_helper(array, m+1, r)
    merge(array, l, m, r)


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)

def quick_sort_helper(array, l, r):
    def partition(array, l, r):
        pivot = array[r]
        q = l
        for i in range(l, r):
            if array[i] < pivot:
                array[q], array[i] = array[i], array[q]
                q += 1
        array[q], array[r] = array[r], array[q]
        return q

    if l >= r:
        return

    pivot = partition(array, l, r)
    quick_sort_helper(array, l, pivot - 1)
    quick_sort_helper(array, pivot + 1, r)


def heap_sort(array):
    def heapify_max(array, start, end):
        p_index = start
        l_index = (2 * p_index) + 1
        r_index = l_index + 1
        left_child = array[l_index] if l_index <= end else None
        right_child = array[r_index] if r_index <= end else None

        highest_index = p_index

        highest_index = l_index if left_child and left_child > array[highest_index] else highest_index
        highest_index = r_index if right_child and right_child > array[highest_index] else highest_index

        if highest_index != p_index:
            array[highest_index], array[p_index] = array[p_index], array[highest_index]
            heapify_max(array, highest_index, end)

    def build_max_heap(array):
        last_index = len(array) - 1
        last_parent = last_index // 2
        for i in range(last_parent, -1, -1):
            heapify_max(array, i, last_index)

    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify_max(array, 0, i - 1)


array = [4, 6, 7, 2, 0, 8]
selection_sort(array)
print(array)

array = [4, 6, 7, 2, 0, 8]
insertion_sort(array)
print(array)

array = [4, 6, 7, 2, 0, 8]
bubble_sort(array)
print(array)

array = [4, 6, 7, 2, 0, 8]
merge_sort(array)
print(array)

array = [4, 6, 7, 2, 0, 8]
quick_sort(array)
print(array)

array = [4, 6, 7, 2, 0, 8]
heap_sort(array)
print(array)