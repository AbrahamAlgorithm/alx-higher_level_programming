#!/usr/bin/python3
def weight_average(my_list=[]):
    """print average of a list

    Args:
        my_list: the list

    Returns:
        the average
    """
    new_list = []
    count = 0
    if len(my_list) == 0:
        return (0)
    for m in my_list:
        new_list.append(m[0] * m[1])
        count += m[1]
    return (sum(new_list) / count)
