#!/usr/bin/python3
"""Module that represents a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(x=x, y=y, id=id, width=size, height=size)

    def __str__(self):
        """Returns str represantation of my class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width
                                                 )
