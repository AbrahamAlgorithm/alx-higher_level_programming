#!/usr/bin/python3
"""writing a base geometry class"""


class BaseGeometry:
    """writing a base geometry class"""

    def area(self):
        """It raise an exception for area not def"""
        raise Exception("area() is not implemented")
