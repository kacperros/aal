name = 'Ordered Pair Select  '


def find_nth_smallest(a, b, n):
    j = 0
    k = 0
    i = 1
    a_len = len(a)
    b_len = len(b)
    ret_list = 0 # 0- none finishe, 1-a finished 2-b finished
    while i < n:
        if a[j] > b[k] and k < b_len-1:
            k += 1
        elif a[j] > b[k]:
            j += 1
            ret_list = 2
        elif a[j] < b[k] and j < a_len-1:
            j += 1
        else:
            k += 1
            ret_list = 1
        i += 1
    if ret_list == 0:
        if a[j] < b[k]:
            return a[j]
        else:
            return b[k]
    else:
        if ret_list == 1:
            return b[k-1]
        else:
            return a[j-1]


def calculate_theoretical_complexity(a_len, b_len, n):
    return n
