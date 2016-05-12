name = 'Binary Ordered Select'


def find_nth_smallest(a, b, n):
    return __nth_smallest_recursive(a, b, 0, 0, n)


def __nth_smallest_recursive(a, b, a_index, b_index, n):
    a_len = len(a)
    b_len = len(b)

    if a_index + b_index == n - 1:
        if a_len > a_index and (b_len <= b_index or a[a_index] < b[b_index]):
            return a[a_index]
        else:
            return b[b_index]

    step = int((n - a_index - b_index)/2)
    a_step = a_index + step
    b_step = b_index + step
    if a_len > a_step - 1 and (b_len <= b_step - 1 or a[a_step - 1] < b[b_step - 1]):
        a_index = a_step
    else:
        b_index = b_step
    return __nth_smallest_recursive(a, b, a_index, b_index, n)


def __half_list(list_halved):
    boundary = int(len(list_halved)/2)
    length = len(list_halved)
    return (list_halved[0:boundary], list_halved[boundary : length])