#!/usr/bin/python3
"""This is my module documantation"""


class Rectangle:
    """This is my class documantation"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constuctor function of my class that
        initialize its attributes.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """Calculates the area of rectangle
        Returns:
            int: The size of area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle
        Returns:
            int: The size of the perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __repr__(self):
        """Official string represantation of my class
        Returns:
            (str): The string represantation.
        """
        module = __file__.split("/")[-1][:-3]
        class_name = self.__class__.__name__
        return f"{class_name}({self.__width}, {self.__height})"

    def __str__(self):
        string = ""
        if not self.__width or not self.__height:
            return string
        for _ in range(self.__height):
            string += (f"{self.print_symbol}" * self.__width)
            string += "\n"
        return string[:-1]

    def __del__(self):
        """Called when my class object is deallocated."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
