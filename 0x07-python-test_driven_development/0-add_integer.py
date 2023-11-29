#!/usr/bin/python3
"""
Defines a function for integer addition
"""


def add_integer(a, b=98):
    """to printinteger addition of teo numbers

    Args:
        a: (int/float)the first number
        b: (int/float)the second number pre-set to 98

    Raises:
        TypeError if a and b are not int or float

    Returns:
        the integer addition of a and b
    """
    if (not(isinstance(a, int)
            or isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not(isinstance(b, int) or
            isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
