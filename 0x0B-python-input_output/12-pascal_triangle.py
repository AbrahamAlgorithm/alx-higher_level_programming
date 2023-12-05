#!/usr/bin/python3
"""wrting a function for pascal triangle"""


def pascal_triangle(n):
    """write a pascal triangle

    Args:
        n: the number

    Returns:
        list of list of its pascal numbers
    """
    outer_list = []
    if (n <= 0):
        return (outer_list)
    n = n + 1
    for i in range(1, n):
        if i != 1:
            mey = outer_list[i - 2].copy()
            meya = []
            for a, b in enumerate(mey):
                if a != 0:
                    meya.append(mey[a - 1] + b)
                else:
                    meya.append(1)
            meya.append(1)
            outer_list.append(meya)
        else:
            outer_list.append([1])
    return (outer_list)
