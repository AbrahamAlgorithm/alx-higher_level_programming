#!/usr/bin/python3
def max_integer(my_list=[]):
    """find the max element in list

    Args:
        my_list: the list that contains the int

    Returns:
        return the max element
    """
    if len(my_list) == 0:
        return (None)
    min_value = -10000000
    for i in my_list:
        if i > min_value:
            min_value = i
    return (min_value)
