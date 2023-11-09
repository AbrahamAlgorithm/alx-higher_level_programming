#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """simple delete an element from dictionary

    Args:
        a_dictionary: the dictionary
        key: the key

    Returns:
       return the new dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
