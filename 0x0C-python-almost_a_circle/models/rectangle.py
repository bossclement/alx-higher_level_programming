#!/usr/bin/python3
"""Inherits Base from base module."""
from models.base import Base


class Rectangle(Base):
    """Presentation of a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor that initializes my attributes."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """sets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Retrieves the value of width"""
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        self.__height = value
