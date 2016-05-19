import time
from locale import currency

import copy
from algorithms import binaryOrderedSelect, heapSelect, kOrderedSelect, medianOfMedians, quickSelect, bruteSelect
import utils.generator
import utils.myprettyprint

algorithms = [(kOrderedSelect.find_nth_smallest, True),
              (binaryOrderedSelect.find_nth_smallest, True),
              (medianOfMedians.find_nth_smallest, False),
              (quickSelect.find_nth_smallest, False),
              (heapSelect.find_nth_smallest, False),
              (bruteSelect.find_nth_smallest, False)]


def benchmark(data, useHeapSelect=True, useMedianOfMedians=True, useQuickSelect=True, useKSelect=True,
              useBinarySelect=True):
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
    results.append(__benchmark_algorithm(data, bruteSelect.find_nth_smallest, bruteSelect.name))
    return results


def __benchmark_algorithm(data, selecting_fun, name):
    used_data = copy.copy(data)
    start_time = time.clock()
    result_num = selecting_fun(used_data[0], used_data[1], used_data[2])
    stop_time = time.clock()
    time_taken = stop_time - start_time
    return (len(data[0]), len(data[1]), data[2], time_taken, result_num, name)


def get_full_benchmark():
    #lengths_base = [1, 2.5, 5, 7.5]
    lengths_base = [1, 5]
    # lengths_exp = [10, 100, 1000, 10000, 100000]
    lengths_exp = [10, 50]
    lengths = [int(x * i) for x in lengths_exp for i in lengths_base]
    pairs = []
    for i in range(0, len(lengths)):
        for j in range(0, len(lengths)):
            pairs.append([lengths[i], lengths[j]])
    benchmark_sets = __designate_sets(pairs)
    data_sets = __create_data_from_sets(benchmark_sets)
    print('Data for benchmarking generated')
    benchmark_results = __benchmark_data_sets(data_sets)
    print('Benchmarking completed')
    utils.myprettyprint.benchmark_pretty_print(benchmark_results)


def __designate_sets(pairs):
    # ns = [1, 5, 15, 40, 85, 160, 275, 350, 850, 1250, 3250, 6750, 8500, 15500, 27500, 45000, 65000, 90000, 125000,
    #       160000, 275000, 325000, 450000, 750000, 1200000, 1400000, 150000]
    ns = [1, 40, 70, 100]
    data = []
    for i in range(0, len(ns)):
        data.append([])
        for pair in pairs:
            if pair[0] + pair[1] >= ns[i]:
                data[i].append((pair[0], pair[1], ns[i]))
    return data


def __create_data_from_sets(nsets):
    data = []
    generators = utils.generator.get_generators()
    for i in range(0, len(generators)):
        current_generator = generators[i][0]
        data.append([])
        generator_node = data[i]
        for j in range(0, len(nsets)):
            data[i].append([])
            n_list_node = generator_node[j]
            for data_sets in nsets[j]:
                a_list, b_list = current_generator(data_sets[0], data_sets[1])
                n_list_node.append((a_list, b_list, data_sets[2]))
    return data


def __benchmark_data_sets(data_sets):
    results = []
    for generator_set_idx in range(0, len(data_sets)):
        generator_data = data_sets[generator_set_idx]
        if generator_set_idx < 2:
            for n_index in generator_data:
                result = benchmark(n_index)
                results.append(result)
        else:
            for n_index in generator_data:
                result = benchmark(n_index, useBinarySelect=False, useKSelect=False)
                results.append(result)
    return results