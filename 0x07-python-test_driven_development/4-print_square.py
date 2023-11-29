#!/usr/bin/python3
"""
This is a module for printing square with #
"""


def print_square(size):
    """printing of square with #

    Args:
         size: (int always) >= 0
    Raises
        TypeError: if the size is not int
        ValueError: if the size is less than error
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("") 
