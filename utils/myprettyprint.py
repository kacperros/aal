import utils.generator

def my_pretty_print(results):
    for result_cell in results:
        for result_subcell in result_cell:
            print("+Algorithm Used: ", result_subcell[5], "\tNumber found: ", '%10d' % result_subcell[4],
                  "\tTime taken [s]: ", '%20.9f' % result_subcell[3], "\tList A length: ", '%10d' % result_subcell[0],
                  "\tList B length: ", '%10d' % result_subcell[1], "\tN: ", '%10d' % result_subcell[2])


def benchmark_pretty_print(benchmark_results):
    generators = utils.generator.get_generators()
    i = 0
    for result_list in benchmark_results:
            print(generators[i % 4][2])
            my_pretty_print(result_list)
            i += 1


def print_summary(results):
    pass