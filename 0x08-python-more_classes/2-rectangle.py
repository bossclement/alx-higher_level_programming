#!/usr/bin/python3
"""This is my module documantation"""


class Rectangle:
    """This is my class documantation"""
    def __init__(self, width=0, height=0):
        """Constuctor function of my class that
        initialize its attributes.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets the value of my width attribute
        Returns:
            int: the value of my width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set a value to my width attribute

        Args:
            value (int): the new value of my width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value of my height attribute
        Returns:
            int: the value of my height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set a value to my height attribute

        Args:
            value (int): the new value of my height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2
