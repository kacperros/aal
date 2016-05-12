import sys
import getopt

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
           'aal -a a_file.txt -b b_file.txt -n 120 -M -Q' \
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
    opts_args = setArgsFromOpts(opts, args)
    validate_options_combination(opts_args)
    print(opts_args)
    print('Input file is ', opts_args.get("a"))
    print('Output file is ', opts_args.get("b"))


def setArgsFromOpts(opts, args):
    result = {}
    k_order = False
    medians = False
    binary = False
    quick = False
    heap = False
    for opt, arg in opts:
        if opt == '-h':
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
            result.update({"c", True})
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
    if not (k_order or medians or binary or quick or heap):
        result.update({"K": True, "M": True, "B": True, "Q": True, "H": True})
    else:
        result.update({"K": k_order, "M": medians, "B": binary, "Q": quick, "H": heap})
    return result


def validate_options_combination(opts_args):
    pass

if __name__ == "__main__":
    main(sys.argv[1:])
