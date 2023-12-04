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
