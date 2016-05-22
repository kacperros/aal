import math


name = 'Brute Force Select       '


def find_nth_smallest(a, b, n):
    data = a + b
    __merge_sort(data)
    return data[n-1]


def __merge_sort(data):
    if len(data) > 1:
        mid_index = len(data) // 2
        left_half = data[:mid_index]
        right_half = data[mid_index:]
        __merge_sort(left_half)
        __merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1


def calculate_theoretical_complexity(a_len, b_len, n):
    return (a_len + b_len) * math.log2(a_len + b_len)
