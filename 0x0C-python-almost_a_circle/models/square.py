#!/usr/bin/python3
"""Module that represents a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(x=x, y=y, id=id, width=size, height=size)
        self.__size = size

    def __str__(self):
        """Returns str represantation of my class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width
                                                 )

    @property
    def size(self):
        """Retrieves the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
