#!/usr/bin/python3
"""Docs for my module goes here"""


class BaseGeometry:
    """Docs for my class goes here"""

    def area(self):
        """Raise Exception Error"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raise Exceptions"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
