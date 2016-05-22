import random


name = 'Quick Select           '


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


def _select(vector, left, right, n):
    while True:
        if left == right:
            return vector[left]
        pivot_index = random.randint(left, right)
        pivot_index = _partition(vector, left, right, pivot_index)
        if n == pivot_index:
            return vector[n]
        elif n < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1


def find_nth_smallest(A, B, n):
    vector = A+B
    n -= 1
    return _select(vector, 0, len(vector)-1, n)


def calculate_theoretical_complexity(a_len, b_len, n):
    z = a_len + b_len
    return _calculate_theoretical_complexity(z)


def _calculate_theoretical_complexity(z):
    if z < 1:
        return 0
    else:
        return z + _calculate_theoretical_complexity(int(z/2))