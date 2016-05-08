import math


def find_nth_smallest(A, B, n):
    vector = A+B
    n -= 1
    return vector[_select(vector, 0, len(vector)-1, n)]


def _select(vector, left, right, n):
    while True:
        if left == right:
            return left
        pivot_index = _pivot(vector, left, right)
        pivot_index = _partition(vector, left, right, pivot_index)
        if n == pivot_index:
            return n
        elif n < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1


def _partition(vector, left, right, pivot_index):
    pivot_value = vector[pivot_index]
    vector[pivot_index], vector[right] = vector[right], vector[pivot_index]
    store_index = left
    for i in range(left, right):
        if vector[i] < pivot_value:
            vector[store_index], vector[i] = vector[i], vector[store_index]
            store_index += 1
    vector[right], vector[store_index] = vector[store_index], vector[right]
    return store_index


def _pivot(vector, left, right):
    if right - left < 5:
        return __partition5(vector, left, right)
    for i in range(left, right, 5):
        sub_right = i + 4
        if sub_right > right:
            sub_right = right
        median5 = __partition5(vector, left, sub_right)
        vector[median5], vector[left + math.floor((i - left)/5)] = \
            vector[left + math.floor((i - left)/5)], vector[median5]
    return _select(vector, left, left + math.ceil((right - left)/5) - 1, left + int((right - left)/10))


def __partition5(vector, left, right):
    for i in range(left, right):
        x = vector[i]
        j = i - 1
        while j >= 0 and vector[j] > x:
            vector[j+1] = vector[j]
            j -= 1
        vector[j+1] = x
    return math.ceil(left + (right - left)/2)
