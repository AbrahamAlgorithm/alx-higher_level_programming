#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """muliply the value in a dictionary

    Args:
        a_dictionary: a dictionary

    Returns:
       the new dictionary with modified value
    """
    new_dict = {}
    for i in a_dictionary:
        new_dict[i] = a_dictionary[i] * 2
    return (new_dict)
