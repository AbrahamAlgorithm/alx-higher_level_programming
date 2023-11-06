#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Check for divisibility by 2

    Args:
        my_list: the list of int

    Returns:
        return the bool value of result
    """
    new_list = []
    for i in my_list:
        new_list.append(i % 2 == 0)
    return (new_list)
