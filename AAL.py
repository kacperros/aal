import ast
import fileinput
import sys
import getopt
from pprint import pprint

import utils.fileHelper
import utils.Benchmark
import utils.generator
import utils.myprettyprint

help_str = 'Well, you seem to have gotten it a tad mixed up.\n ' \
           'So here is the drill: \n' \
           'aal -h \t\t will show this text \n\n' \
           'aal -a <a_list_file> -b <b-list_file> -n <searched_number> \t this will use all the algorithms \n' \
           'and print results for them. You can further specify algorithms you wish to use through options: \n' \
           '-K\t a O(k) algorithm comparing pairs !Use this only with sorted lists!\n' \
           '-M\t The median of medians algorithms \n' \
           '-Q\t The quickSelect algorithm \n' \
           '-B\t The binary select algorithm !Use only with sorted lists!\n' \
           '-H\t The modified heap select algorithm\n\n' \
           'input from stdin is also accepted as long as it adehers to the following rule:\n' \
           '[([a1,a2,...,ak],[b1,b2,...,bm],n),(...)] and flag -c is used\n' \
           'Loaded files follow a similar syntax:\n' \
           '[[a1,a2,...ak],[...]]\n' \
           'any number of lists can be loaded but a_file and b_file must contain the same number of lists\n\n' \
           'In case you dear user may require a tad of help generating the numbers:\n' \
           '-g\t This option requires that you provide one of the following strings:\n' \
           '\t\t ordered_positive\n' \
           '\t\t ordered_natural\n' \
           '\t\t unordered_positive\n' \
           '\t\t unordered_natural\n' \
           'Then provide all five flags: -f, -t, -F, -T, -S with parameters:\n' \
           '-f,-F \tflags stating the starting number of elements for list A and B\n' \
           '-t,-T \tflags stating the ending biggest number of elements for list A and B\n' \
           '-S \tflags stating the number of steps in which to divide F-T and f-t\n' \
           'The final input option is to use the stdin in order to provide tuples -m flag:\n' \
           '[(a_size, b_size,n),(...)] together with the -g flag. \n\n' \
           'And last but not least the benchmark test! Use it with caution for it\n' \
           'takes some time. Fired up? Alright! To start the benchmark simply use:\n' \
           'aal --benchmark' \
           'Some valid examples:\n' \
           'aal -a a_file.txt -b b_file.txt -n 150\n' \
           'aal -a a_file.txt -b b_file.txt -n 120 -M -Q\n' \
           'aal -c\n' \
           'aal -m\n' \
           'aal -g ordered_positive -f 150 -t 300 -F 50 -T 100 -S 4 -n 170\n' \
           'aal -- benchmark\n\n' \
           'Author: Kacper Roszczyna, WUT\n' \
           'License: MIT'


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ha:b:n:KMBQHcg:f:t:F:T:S:m", ['benchmark'])
    except getopt.GetoptError:
        print(help_str)
        sys.exit(2)
    opts_args = _setArgsFromOpts(opts, args)
    _execute_with_opts(opts_args)



def _setArgsFromOpts(opts, args):
    result = {}
    k_order = False
    medians = False
    binary = False
    quick = False
    heap = False
    for opt, arg in opts:
        if opt == "-h":
            result.update({"h": True})
        elif opt == "-a":
            result.update({"a": arg})
        elif opt == "-b":
            result.update({"b": arg})
        elif opt == "-n":
            result.update({"n": arg})
        elif opt == "-K":
            k_order = True
        elif opt == "-M":
            medians = True
        elif opt == "-H":
            heap = True
        elif opt == "-Q":
            quick = True
        elif opt == "-B":
            binary = True
        elif opt == "-c":
            result.update({"c": True})
        elif opt == "-g":
            result.update({"g": arg})
        elif opt == "-f":
            result.update({"f": arg})
        elif opt == "-t":
            result.update({"t": arg})
        elif opt == "-F":
            result.update({"F": arg})
        elif opt == "-T":
            result.update({"T": arg})
        elif opt == "-S":
            result.update({"S": arg})
        elif opt == "-m":
            result.update({"m": arg})
        elif opt == "--benchmark":
            result.update({"benchmark": True})
    if not (k_order or medians or binary or quick or heap):
        result.update({"K": True, "M": True, "B": True, "Q": True, "H": True})
    else:
        result.update({"K": k_order, "M": medians, "B": binary, "Q": quick, "H": heap})
    return result


def _execute_with_opts(opts_args):
    data = []
    if opts_args.get("h"):
        print(help_str)
        sys.exit(0)
    if opts_args.get("a") is not None and opts_args.get("b") is not None and opts_args.get("n") is not None:
        data.extend(__prep_data_from_ab_files(opts_args))
    if opts_args.get("c"):
        data.extend(__prep_data_from_input())
    print(data)
    if opts_args.get("g"):
        generator_type = __get_generator(opts_args.get("g"))
        if opts_args.get("f") is not None and opts_args.get("t") is not None and opts_args.get("F") is not None \
                and opts_args.get("T") is not None and opts_args.get("S") is not None and opts_args.get("n") is not None:
            data.extend(__generate_data_in_intervals(opts_args.get("f"), opts_args.get("t"), opts_args.get("F"),
                                                     opts_args.get("T"), opts_args.get("S"),
                                                     generator_type, opts_args.get("n")))
        if opts_args.get("m") is not None:
            data.extend(__generate_data_from_input(generator_type))
    if opts_args.get("benchmark"):
        data = __produce_benchmark_data()
    result = utils.Benchmark.benchmark(data, useBinarySelect=opts_args.get("B"),
                                       useHeapSelect=opts_args.get("H"),
                                       useKSelect=opts_args.get("K"),
                                       useMedianOfMedians=opts_args.get("M"),
                                       useQuickSelect=opts_args.get("Q"))
    utils.myprettyprint.my_pretty_print(result)
    utils.myprettyprint.print_summary(result)


def __prep_data_from_ab_files(opts_args):
    a_lists = utils.fileHelper.read_ab_file(opts_args.get("a"))
    b_lists = utils.fileHelper.read_ab_file(opts_args.get("b"))
    n = opts_args.get("n")
    if len(a_lists) != len(b_lists):
        print("Given files do not contain the same lengths of lists")
        sys.exit(2)
    data = __build_data(a_lists, b_lists, n)
    return data


def __build_data(a_lists, b_lists, n):
    data = []
    for i in range(0, len(a_lists)):
        if int(n) > len(a_lists[i]) + len(b_lists[i]):
            print("n must be less then both lists combined in length!")
            sys.exit(2)
        data.append((a_lists[i], b_lists[i], int(n)))
    return data


def __prep_data_from_input():
    data = ''
    for line in sys.stdin:
        data += line
    data = ast.literal_eval(data)
    return data


def __get_generator(gen):
    if gen == "ordered_positive":
        return utils.generator.generate_ordered_positive
    elif gen == "ordered_natural":
        return utils.generator.generate_ordered_full_range
    elif gen == "unordered_positive":
        return utils.generator.generate_unordered_positive
    elif gen == "unordered_natural":
        return utils.generator.generate_unordered_full_range
    else:
        print("Incorrect generator option. Exiting")
        sys.exit(2)


def __generate_data_in_intervals(a_start, a_stop, b_start, b_stop, num_of_intervals, generator_type, n):
    results = []
    a_start = int(a_start)
    a_stop = int(a_stop)
    b_start = int(b_start)
    b_stop = int(b_stop)
    num_of_intervals = int(num_of_intervals)
    if a_stop < a_start or b_stop < b_start or num_of_intervals > a_stop - a_start or num_of_intervals > b_stop - b_start:
        print("Incorrect interval configuration or start stop index configuration")
        sys.exit(2)
    n = int(n)
    a_step = int((a_stop - a_start)/num_of_intervals)
    a_lengths_list = [a_start + x*a_step for x in range(0, num_of_intervals)]
    b_step = int((b_stop - b_start)/num_of_intervals)
    b_length_list = [b_start + y*b_step for y in range(0, num_of_intervals)]
    for i in range(0, num_of_intervals):
        a_list, b_list = generator_type(a_lengths_list[i], b_length_list[i])
        results.append((a_list, b_list, n))
    return results


def __generate_data_from_input(generator_type):
    data = ''
    returned_data = []
    for line in sys.stdin:
        data += line
    data = ast.literal_eval(data)
    for data_node in data:
        if int(data_node[0]) + int(data_node[1]) < int(data_node[2]):
            print("Skipping ", data_node)
            continue
        a_list, b_list = generator_type(int(data_node[0]), int(data_node[1]))
        returned_data.append((a_list, b_list, int(data_node[2])))
    return returned_data


def __produce_benchmark_data():
    return utils.Benchmark.get_full_benchmark()


if __name__ == "__main__":
    main(sys.argv[1:])
