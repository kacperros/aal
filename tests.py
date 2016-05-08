import heapSelect
import medianOfMedians
import orderedSelects
import quickSelect

A = [1796, -1395, -1001, -1112, -980, 437, -2081, 364, 1261, 752, -1039, -1166, 2677]
B = [272, 1586, 65, 1746, 854, -2088, -791, 367, 503, -2306, 126]

print("Testing heap Sorts")
n_max_heap = 20
n_min_heap = 5
print(heapSelect.find_nth_smallest(A, B, n_min_heap))
assert(heapSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(heapSelect.find_nth_smallest(A, B, n_max_heap))
assert(heapSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("QuickSelect")
print(quickSelect.find_nth_smallest(A, B, n_min_heap))
assert(quickSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(quickSelect.find_nth_smallest(A, B, n_max_heap))
assert(quickSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("MedianOfMedians")
print(medianOfMedians.find_nth_smallest(A, B, n_min_heap))
assert(medianOfMedians.find_nth_smallest(A, B, n_min_heap) == -1166)
print(medianOfMedians.find_nth_smallest(A, B, n_max_heap))
assert(medianOfMedians.find_nth_smallest(A, B, n_max_heap) == 1261)
assert(medianOfMedians.find_nth_smallest(A,B, 4) == -1395)

print("Testing ordered Sorts")
A.sort()
B.sort()
print("Heap Sorts")
print(heapSelect.find_nth_smallest(A, B, n_min_heap))
assert(heapSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(heapSelect.find_nth_smallest(A, B, n_max_heap))
assert(heapSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("Ordered Sorts O(k)")
print(orderedSelects.find_nth_smallest(A, B, n_min_heap))
assert(orderedSelects.find_nth_smallest(A, B, n_min_heap) == -1166)
print(orderedSelects.find_nth_smallest(A, B, n_max_heap))
assert(orderedSelects.find_nth_smallest(A, B, n_max_heap) == 1261)
print("Binary Searches")
print(orderedSelects.binary_find_nth_smallest(A, B, n_min_heap))
assert(orderedSelects.binary_find_nth_smallest(A, B, n_min_heap) == -1166)
print(orderedSelects.binary_find_nth_smallest(A, B, n_max_heap))
assert(orderedSelects.binary_find_nth_smallest(A, B, n_max_heap) == 1261)
print("QuickSelect")
print(quickSelect.find_nth_smallest(A, B, n_min_heap))
assert(quickSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(quickSelect.find_nth_smallest(A, B, n_max_heap))
assert(quickSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("MedianOfMedians")
print(medianOfMedians.find_nth_smallest(A, B, n_min_heap))
assert(medianOfMedians.find_nth_smallest(A, B, n_min_heap) == -1166)
print(medianOfMedians.find_nth_smallest(A, B, n_max_heap))
assert(medianOfMedians.find_nth_smallest(A, B, n_max_heap) == 1261)
assert(medianOfMedians.find_nth_smallest(A,B, 4) == -1395)
