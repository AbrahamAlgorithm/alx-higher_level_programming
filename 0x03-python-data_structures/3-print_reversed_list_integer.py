#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print list in reverse order

    Args:
        my_list: the list to reverse

    Returns:
        Null
    """
    if my_list is None:
        return ('')
    if len(my_list) == 0:
        return ('')
    for i in range(int(len(my_list) / 2)):
        ldx = len(my_list) - i - 1
        elem = my_list[ldx]
        my_list[ldx] = my_list[i]
        my_list[i] = elem
    for i in my_list:
        print("{:d}".format(i))
