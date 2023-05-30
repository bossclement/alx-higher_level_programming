#!/usr/bin/python3
"""
Documantation for the module
"""


class Square:
    """Class docstring"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor function
        Args:
            size (:obj: `int`, optional): size of the side of a
                a square.
            position (tuple): coordinates of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of the square
        Returns:
            int: area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Retrives the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints my square"""
        s = "" if self.__position[1] > 0 else (" " * self.__position[0])
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            if s:
                print("{}{}".format(s, ("#" * self.__size)))
            else:
                print("#" * self.__size)
        if self.__size == 1:
            print("#")

    @property
    def position(self):
        """Retrieves the value if position
        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set value to position attribute
        Args:
            value (tuple): the value to use
        Raises:
            TypeError: if value doesn't have 2 positive
                integers in it
        """
        if (not value or len(value) != 2) or \
                (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
