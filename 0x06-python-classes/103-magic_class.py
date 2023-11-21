#!/usr/bin/python3
"""interpret a python class code bytecode"""

import math


class MagicClass:
    """the Magicclass decode"""

    def __init__(self, radius=0):
        """the init class of magicclass"""
        self.__radius = 0
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculate the arear of the circle"""
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """calculate the circumference"""
        return ((2 * math.pi) * self.__radius)
