name = 'Median of Medians'


def find_nth_smallest(A, B, n):
    vector = A+B
    n -= 1
    return select(vector, n)


def select(vector, n):
    if len(vector) < 10:
        vector.sort()
        return vector[n]
    group_five_vector = []
    left_index = 0
    while left_index+5 < len(vector)-1:
        group_five_vector.append(vector[left_index:left_index + 5])
        left_index += 5
    group_five_vector.append(vector[left_index:])
    medians = []
    for subList in group_five_vector:
        medians.append(select(subList, int((len(subList)-1)/2)))
    med = select(medians, int((len(medians)-1)/2))
    less_list = []
    equal_list = []
    greater_list = []
    for i in vector:
        if i < med:
            less_list.append(i)
        elif i > med:
            greater_list.append(i)
        else:
            equal_list.append(i)
    if n < len(less_list):
        return select(less_list, n)
    elif n < len(equal_list) + len(less_list):
        return equal_list[0]
    else:
        return select(greater_list, n - len(less_list) - len(equal_list))