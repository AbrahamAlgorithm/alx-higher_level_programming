#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """complex delete in a dictionary

    Args:
        a_dictionary: the dictionary
        value in the dictionary

    Returns:
        the dictionary with change value
    """
    new_list = []
    for i, j in a_dictionary.items():
        if j == value:
            new_list.append(i)
    for m in new_list:
        del a_dictionary[m]
    return (a_dictionary)
