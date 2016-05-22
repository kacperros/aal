import utils.generator
import utils.Benchmark
import statistics


def my_result_print(results):
    algos = utils.Benchmark.algorithms
    i = 0
    for algorithms in results:
        median_index = int(len(algorithms)/2)
        for result_subcell in algorithms:
            result_subcell.append(__calculate_q(result_subcell, algorithms[median_index]))
            pretty_print_result(result_subcell)
        i += 1


def __calculate_q(result_cell, median):
    algorithm = utils.Benchmark.algorithms_dict.get(result_cell[5])
    q = (result_cell[3] * algorithm[2](median[0], median[1], median[2])) / (algorithm[2](median[0], result_cell[1],
                                                                                        result_cell[2]) * median[3])
    return q


def pretty_print_result(result):
    print("+Algorithm Used: ", result[5],
          "\tNumber found: ", '%10d' % result[4],
          "\tTime taken [s]: ", '%20.9f' % result[3],
          "\tList A length: ", '%10d' % result[0],
          "\tList B length: ", '%10d' % result[1],
          "\tN: ", '%10d' % result[2],
          "\tq: ", '%2.3f' % result[6]
          )


def benchmark_pretty_print(benchmark_results):
    i = 0
    k = 0
    step = 20
    generators = utils.generator.get_generators()
    algorithms = utils.Benchmark.algorithms
    for generator_node in benchmark_results:
        print(generators[i][2])
        for algorithm_node in generator_node:
            medians = __select_medians(algorithm_node, step)
            if len(algorithm_node) == 0:
                k += 1
                continue
            print(algorithm_node[k % len(algorithms)][5])
            for results_node in algorithm_node:
                results_node.append(__calculate_q(results_node, __get_proper_median(results_node, medians)))
                pretty_print_result(results_node)
            k += 1
        i += 1


def __select_medians(algorithm_node, step):
    half_step = int(step/2)
    medians = []
    for i in range(0, int(len(algorithm_node)/step)):
        medians.append(algorithm_node[half_step + i*step - 1])
    return medians


def __get_proper_median(result_node,medians):
    for median in medians:
        if result_node[0] == median[0] and result_node[1] == median[1]:
            return median