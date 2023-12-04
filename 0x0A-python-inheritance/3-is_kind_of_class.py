#!/usr/bin/python3
"""check if it is instance of class and inheritance"""


def is_kind_of_class(obj, a_class):
    """is kind of class through inheritance or anything

    Args:
        obj: the object to check
        a_class: the class to check from

    Returns:
        True if and false else
    """
    return (isinstance(obj, a_class))
