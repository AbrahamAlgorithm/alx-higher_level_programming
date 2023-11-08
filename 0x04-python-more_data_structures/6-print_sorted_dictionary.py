#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print sorted dictionary

    Args:
        a_dictionary: the dictionary

    Returns:
         nothing
    """
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
