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
        if type(value) is not int:
            raise TypeError("Value is not an intiger")
        elif value <= 0:
            raise ValueError("Value is <= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) is not int:
            raise TypeError("Value is not an intiger")
        elif value <= 0:
            raise ValueError("Value is <= 0")
        self.__height = value

    @property
    def y(self):
        """Retrieves the value of y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        self.__y = value

    @property
    def x(self):
        """Retrieves the value of x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        self.__x = value
