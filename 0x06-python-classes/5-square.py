#!/usr/bin/python3
"""The square module continue"""


class Square:
    """The class to create square."""

    def __init__(self, size=0):
        """set size to private instance variable

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """get the area of the square

        Args:
            None

        Returns:
            Area of the square(int)
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """getter that get size variable"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set thesize to the value

        Args:
            value: the value to reset
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print square form the size"""
        value = self.__size
        for i in range(value):
            [print('#', end='') for j in range(value)]
            print('')
        if value == 0:
            print('')
