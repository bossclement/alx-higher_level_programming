#!/usr/bin/python3
"""
This is the documentation for this module
"""
import math


class MagicClass:
    """My class"""
    def __init__(self, radius):
        """My constructor"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates area"""
        return 2 * math.pi * self.__radius

    def circumference(self):
        """Gets the circumference"""
        return 2 * math.pi * self.__radius
