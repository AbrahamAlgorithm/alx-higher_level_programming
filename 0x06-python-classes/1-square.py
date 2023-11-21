#!/usr/bin/python3
"""Square and set size as private instance variable"""


class Square:
    """The class to create square."""

    def __init__(self, size):
        """Initialzes size to piV

        Args:
            size (int): the size of the square
        """
        self.__size = size
