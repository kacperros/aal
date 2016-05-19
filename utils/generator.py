import random


def get_generators():
    return [(generate_ordered_positive, True, 'Ordered Positives Generator'),
            (generate_ordered_full_range, True, 'Ordered Natural Generator'),
            (generate_unordered_positive, False, 'Unordered Positives Generator'),
            (generate_unordered_full_range, False, 'Unordered Natural Generator')]


def generate_ordered_positive(n, m):
    lower_bound = 0
    upper_bound = 2 * n * round(random.randint(50, 100))
    result = _generate_ordered(n + m, lower_bound, upper_bound)
    return __divide_into_lists(result, n, m)


def generate_ordered_full_range(n, m):
    lower_bound = -2 * n * round(random.randint(50, 100))
    upper_bound = 2 * n * round(random.randint(50, 100))
    result = _generate_ordered(n + m, lower_bound, upper_bound)
    return __divide_into_lists(result, n, m)


def _generate_ordered(n, lower_bound, upper_bound):
    generated_values = __generate(n, lower_bound, upper_bound)
    generated_values.sort()
    return generated_values


def generate_unordered_positive(n, m):
    lower_bound = 0
    upper_bound = 2 * n * round(random.randint(5, 100))
    result = _generate_unordered(n + m, lower_bound, upper_bound)
    return __divide_into_lists(result, n, m)


def generate_unordered_full_range(n, m):
    lower_bound = -2 * n * round(random.randint(50, 100))
    upper_bound = 2 * n * round(random.randint(50, 100))
    result = _generate_unordered(n + m, lower_bound, upper_bound)
    return __divide_into_lists(result, n, m)


def _generate_unordered(n, lower_bound, upper_bound):
    return __generate(n, lower_bound, upper_bound)


def __generate(n, lower_bound, upper_bound):
    generated_values = set()
    while len(generated_values) < n:
        generated_values.add(random.randint(lower_bound, upper_bound))
    generated_values = list(generated_values)
    return generated_values


def __divide_into_lists(result, n, m):
    A = []
    B = []
    for i in range(0, n + m):
        coin = random.randint(1, 2)
        if coin == 1 and len(A) < n:
            A.append(result[i])
        elif coin == 2 and len(B) < m:
            B.append(result[i])
        elif len(A) < n:
            A.append(result[i])
        else:
            B.append(result[i])
    return (A, B)
