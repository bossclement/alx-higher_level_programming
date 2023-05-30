#!/usr/bin/python3
"""
Documantation for the module
"""


class Square:
    """Class docstring"""

    def __init__(self, size=0):
        """Constructor function"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
