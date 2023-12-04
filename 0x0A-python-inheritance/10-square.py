#!/usr/bin/python3
"""writing a base geometry class"""


class BaseGeometry:
    """writing a base geometry class"""

    def area(self):
        """It raise an exception for area not def"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation of value for int and > 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class inherit from base geometry"""

    def __init__(self, width, height):
        """a constructor class for rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area"""
        return (self.__width * self.__height)

    def __str__(self):
        """declaring the print"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """the square modulo"""

    def __init__(self, size):
        """constructor for square"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
