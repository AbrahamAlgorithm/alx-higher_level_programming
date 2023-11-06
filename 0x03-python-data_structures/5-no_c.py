#!/usr/bin/python3
def no_c(my_string):
    """return string without c and C

    Args:
        my_string: the string

    Returns:
        a new string without c and C
    """
    new_string = ''
    for i in range(len(my_string)):
        if my_string[i] not in 'cC':
            new_string += my_string[i]
    return (new_string)
