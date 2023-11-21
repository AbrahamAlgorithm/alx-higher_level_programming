#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """safe print of the list

    Args:
        my_list: the list
        x: the number of elemnt to print

    Returns:
        the number of the element printed truly
    """
    if my_list is None or x < 0:
        return (0)
    i = 0
    try:
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
    except IndexError:
        print("")
        return (i)
    print("")
    return (i)
