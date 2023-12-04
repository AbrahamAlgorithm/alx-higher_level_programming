#!/usr/bin/python3
"""the object is an instance of a class that inherited
(directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """check if it inherited instance of that class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
