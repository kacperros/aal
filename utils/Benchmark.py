import time
from locale import currency

import copy
from algorithms import binaryOrderedSelect, heapSelect, kOrderedSelect, medianOfMedians, quickSelect, bruteSelect
import utils.generator
import utils.myprettyprint


algorithms = [(kOrderedSelect.find_nth_smallest, True, kOrderedSelect.name, kOrderedSelect.calculate_theoretical_complexity),
              (binaryOrderedSelect.find_nth_smallest, True, binaryOrderedSelect.name, binaryOrderedSelect.calculate_theoretical_complexity),
              (medianOfMedians.find_nth_smallest, False, medianOfMedians.name, medianOfMedians.calculate_theoretical_complexity),
              (quickSelect.find_nth_smallest, False, quickSelect.name, quickSelect.calculate_theoretical_complexity),
              (heapSelect.find_nth_smallest, False, heapSelect.name, heapSelect.calculate_theoretical_complexity),
              (bruteSelect.find_nth_smallest, False, bruteSelect.name, bruteSelect.calculate_theoretical_complexity)]

algorithms_dict = {kOrderedSelect.name: [kOrderedSelect.find_nth_smallest, True,  kOrderedSelect.calculate_theoretical_complexity],
                  binaryOrderedSelect.name : [binaryOrderedSelect.find_nth_smallest, True, binaryOrderedSelect.calculate_theoretical_complexity],
                  medianOfMedians.name: [medianOfMedians.find_nth_smallest, False,medianOfMedians.calculate_theoretical_complexity],
                  quickSelect.name: [quickSelect.find_nth_smallest, False,quickSelect.calculate_theoretical_complexity],
                  heapSelect.name: [heapSelect.find_nth_smallest, False,heapSelect.calculate_theoretical_complexity],
                  bruteSelect.name: [bruteSelect.find_nth_smallest, False,bruteSelect.calculate_theoretical_complexity]}


def benchmark(data, useHeapSelect=True, useMedianOfMedians=True, useQuickSelect=True, useKSelect=True,
              useBinarySelect=True):
    results = [[], [], [], [], [], []]
    for i in range(0, len(data)):
        operated_data = copy.copy(data[i])
        result = _test_single_data_set(operated_data, useHeapSelect, useMedianOfMedians, useQuickSelect,
                                       useKSelect, useBinarySelect)
        __append_to_results(result, results)
    return results


def __append_to_results(result, results):
    i = 0
    for result_element in result:
        results[i].append(result_element)
        i += 1


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
    return [len(data[0]), len(data[1]), data[2], time_taken, result_num, name]


def get_full_benchmark():
    lengths_base = [10, 20]
    lengths_exp = [50, 100, 200]
    lengths = list(set([int(x * i) for x in lengths_exp for i in lengths_base]))
    pairs = []
    for i in range(0, len(lengths)):
        for j in range(i, len(lengths)):
            pairs.append([lengths[i], lengths[j]])
    data_sets = __create_data_from_pairs(pairs)
    print('Data for benchmarking generated')
    benchmark_results = __benchmark_data_sets(data_sets)
    print('Benchmarking completed')
    utils.myprettyprint.benchmark_pretty_print(benchmark_results)


def __create_data_from_pairs(pairs):
    data = []
    generators = utils.generator.get_generators()
    for i in range(0, len(generators)):
        current_generator = generators[i][0]
        generator_node = []
        for pair in pairs:
            a_list, b_list = current_generator(pair[0], pair[1])
            n_step = int((pair[0]+pair[1])/21)
            ns = [i*n_step for i in range(1, 21)]
            pair_node = [(a_list, b_list, n) for n in ns]
            generator_node.append(pair_node)
        data.append(generator_node)
    return data


def __benchmark_data_sets(data_sets):
    results = []
    i = 0
    for generator_node in data_sets:
        result_generator_node = []
        for algorithm in algorithms:
            algorithm_node = []
            for pair_node in generator_node:
                for single_pair in pair_node:
                    if i < 2:
                        result_algorithm_pair_node = __benchmark_algorithm(single_pair, algorithm[0], algorithm[2])
                        algorithm_node.append(result_algorithm_pair_node)
                    else:
                        if algorithm[2] == kOrderedSelect.name or algorithm[2] == binaryOrderedSelect.name:
                            continue
                        result_algorithm_pair_node = __benchmark_algorithm(single_pair, algorithm[0], algorithm[2])
                        algorithm_node.append(result_algorithm_pair_node)
            result_generator_node.append(algorithm_node)
        i += 1
        results.append(result_generator_node)
    return results
