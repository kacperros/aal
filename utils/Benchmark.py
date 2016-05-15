import time

import copy
from algorithms import binaryOrderedSelect, heapSelect, kOrderedSelect, medianOfMedians, quickSelect


def benchmark(data, useHeapSelect=True, useMedianOfMedians=True, useQuickSelect=True, useKSelect=True, useBinarySelect=True):
    results = []
    for i in range(0, len(data)):
        operated_data = copy.copy(data[i])
        result = _test_single_data_set(operated_data, useHeapSelect, useMedianOfMedians, useQuickSelect,
                                       useKSelect, useBinarySelect)
        results.append(result)
    return results


def _test_single_data_set(data, useHeapSelect=True, useMedianOfMedians=True, useQuickSelect=True,
                          useKSelect=True, useBinarySelect=True):
    results = []
    if useHeapSelect:
        result = __benchmark_algorithm(data, heapSelect.find_nth_smallest, heapSelect.name)
        results.append(result)
    if useMedianOfMedians:
        result = __benchmark_algorithm(data, medianOfMedians.find_nth_smallest, medianOfMedians.name)
        results.append(result)
    if useQuickSelect:
        result = __benchmark_algorithm(data, quickSelect.find_nth_smallest, quickSelect.name)
        results.append(result)
    if useKSelect:
        result = __benchmark_algorithm(data, kOrderedSelect.find_nth_smallest, kOrderedSelect.name)
        results.append(result)
    if useBinarySelect:
        result = __benchmark_algorithm(data, binaryOrderedSelect.find_nth_smallest, binaryOrderedSelect.name)
        results.append(result)
    return results


def __benchmark_algorithm(data, selecting_fun, name):
    used_data = copy.copy(data)
    start_time = time.clock()
    result_num = selecting_fun(used_data[0], used_data[1], used_data[2])
    stop_time = time.clock()
    time_taken = stop_time - start_time
    return(len(data[0]), len(data[1]), data[2], time_taken, result_num, name)