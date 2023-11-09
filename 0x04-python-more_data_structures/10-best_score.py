#!/usr/bin/python3
def best_score(a_dictionary):
    """the highest score in a dictionary

    Args:
        a_dictionary: the dictionary

    Returns:
        the key of highest score in a dictionary
    """
    high = -1000000
    key = ''
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    for elem in a_dictionary:
        if a_dictionary[elem] > high:
            high = a_dictionary[elem]
            key = elem
    return (key)
