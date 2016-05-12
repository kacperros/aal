import Benchmark
import generator
from algorithms import binaryOrderedSelect, heapSelect, kOrderedSelect, medianOfMedians, quickSelect

A = [1796, -1395, -1001, -1112, -980, 437, -2081, 364, 1261, 752, -1039, -1166, 2677]
B = [272, 1586, 65, 1746, 854, -2088, -791, 367, 503, -2306, 126]

print("Testing heap Sorts")
n_max_heap = 20
n_min_heap = 5
print(heapSelect.find_nth_smallest(A, B, n_min_heap))
assert (heapSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(heapSelect.find_nth_smallest(A, B, n_max_heap))
assert (heapSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("QuickSelect")
print(quickSelect.find_nth_smallest(A, B, n_min_heap))
assert (quickSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(quickSelect.find_nth_smallest(A, B, n_max_heap))
assert (quickSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("MedianOfMedians")
print(medianOfMedians.find_nth_smallest(A, B, n_min_heap))
assert (medianOfMedians.find_nth_smallest(A, B, n_min_heap) == -1166)
print(medianOfMedians.find_nth_smallest(A, B, n_max_heap))
assert (medianOfMedians.find_nth_smallest(A, B, n_max_heap) == 1261)
assert (medianOfMedians.find_nth_smallest(A, B, 4) == -1395)

print("Testing ordered Sorts")
A.sort()
B.sort()
print("Heap Sorts")
print(heapSelect.find_nth_smallest(A, B, n_min_heap))
assert (heapSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(heapSelect.find_nth_smallest(A, B, n_max_heap))
assert (heapSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("Ordered Sorts O(k)")
print(kOrderedSelect.find_nth_smallest(A, B, n_min_heap))
assert (kOrderedSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(kOrderedSelect.find_nth_smallest(A, B, n_max_heap))
assert (kOrderedSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("Binary Searches")
print(binaryOrderedSelect.find_nth_smallest(A, B, n_min_heap))
assert (binaryOrderedSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(binaryOrderedSelect.find_nth_smallest(A, B, n_max_heap))
assert (binaryOrderedSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("QuickSelect")
print(quickSelect.find_nth_smallest(A, B, n_min_heap))
assert (quickSelect.find_nth_smallest(A, B, n_min_heap) == -1166)
print(quickSelect.find_nth_smallest(A, B, n_max_heap))
assert (quickSelect.find_nth_smallest(A, B, n_max_heap) == 1261)
print("MedianOfMedians")
print(medianOfMedians.find_nth_smallest(A, B, n_min_heap))
assert (medianOfMedians.find_nth_smallest(A, B, n_min_heap) == -1166)
print(medianOfMedians.find_nth_smallest(A, B, n_max_heap))
assert (medianOfMedians.find_nth_smallest(A, B, n_max_heap) == 1261)
assert (medianOfMedians.find_nth_smallest(A, B, 4) == -1395)

a, b = generator.generate_ordered_full_range(500000, 1600000)
n = 530000
benchmark_data = [(a, b, n)]
benchmark_result = Benchmark.benchmark(benchmark_data)
print(benchmark_result)


a = [1,3]
b = [2, 6, 8, 10, 16]
print(kOrderedSelect.find_nth_smallest(a, b, 5))
assert(kOrderedSelect.find_nth_smallest(a, b, 5) == 8)
