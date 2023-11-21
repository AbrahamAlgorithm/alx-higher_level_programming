#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """safe print list integers

    Args:
        my_list: the list
        x: the number of element to print

    Return:
        the real number of integer printed
    """
    if my_list is None or x < 0:
        return (0)
    num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num)
