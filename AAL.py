import random
import heapq
import generator
import orderedSelects

# print(generator.generate_ordered_positive(10))
# print(generator.generate_ordered_full_range(10))
# print(generator.generate_unordered_full_range(10))
# print(generator.generate_unordered_positive(10))

A, B = generator.generate_unordered_full_range(15, 9)
A.sort()
B.sort()
print(A)
print(B)

var = 100
coin = 5
if coin == 5 and var == 100:
    print(1)
elif coin == 5:
    print(2)

