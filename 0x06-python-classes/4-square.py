#!/usr/bin/python3
"""
Documantation for the module
"""


class Square:
    """Class docstring"""

    def __init__(self, size=0):
        """Constructor function"""
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrives the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
