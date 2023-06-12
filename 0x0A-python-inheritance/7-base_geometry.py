#!/usr/bin/python3
"""Docs for my module goes here"""


class BaseGeometry:
    """Docs for my class goes here"""

    def area(self):
        """
        Calculate the area.
        Raises an exception indicating that the area() method is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value.
        Checks if the value is an integer and greater than 0.
        Raises TypeError or ValueError exceptions if the validation fails.

        :param name: The name of the value.
        :param value: The value to validate.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
