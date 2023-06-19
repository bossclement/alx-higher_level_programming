#!/usr/bin/python3
"""Inherits Base from base module."""
from models.base import Base


class Rectangle(Base):
    """Presentation of a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor that initializes my attributes."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """sets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Retrieves the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """Retrieves the value of y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """Retrieves the value of x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """Gets the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Displays the rectangle."""
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="" if w + 1 < self.width else '\n')

    def __str__(self):
        """Returns str represantation of my class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Updates attributes of my class."""
        attributes = ["id", "width", "height", "x", "y"]
        assigned = []
        for index, arg in enumerate(args):
            if index >= len(attributes):
                break
            assigned.append(attributes[index])
            setattr(self, attributes[index], arg)

        not_assigned = set(list(kwargs.keys())).difference(set(assigned))
        for attr in not_assigned:
            setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """Returns certain attributes of my class."""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
