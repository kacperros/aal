import heapq
import math

name = 'Modified Heap Select   '


def find_nth_smallest(a, b, n):
    choice = _verify_use_min_heap(len(a), len(b), n)
    if choice:
        return _min_heap_find(a, b, n)
    else:
        return _max_heap_find(a, b, n)


def _verify_use_min_heap(a_length, b_length, n):
    z = a_length + b_length
    return z ** n < n ** (2 * (z - n))


def _min_heap_find(a, b, n):
    heap = a + b
    heapq.heapify(heap)
    for i in range(0, n - 1):
        heapq.heappop(heap)
    return heapq.heappop(heap)


def _max_heap_find(a, b, n):
    heap, combined_list = __prep_max_heap_sort(a, b, n)
    while combined_list:
        checked = -1 * combined_list.pop()
        if checked > heap[0]:
            heapq.heappushpop(heap, checked)
    return -1 * heap[0]


def __prep_max_heap_sort(a, b, n):
    combined_list = a + b
    list_to_heapify = combined_list[0:n]
    del combined_list[0:n]
    list_to_heapify = [-x for x in list_to_heapify]
    heapq.heapify(list_to_heapify)
    return (list_to_heapify, combined_list)


def calculate_theoretical_complexity(a_len, b_len, n):
    if _verify_use_min_heap(a_len, b_len, n):
        return a_len + b_len + n * math.log2(a_len + b_len)
    else:
        return a_len + b_len + 2 * (a_len + b_len - n) * math.log2(n)
