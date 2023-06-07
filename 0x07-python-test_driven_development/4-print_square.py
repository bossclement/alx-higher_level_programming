#!/usr/bin/python3
"""
In this module there's a function "print_square",
This function prints a square using the '#' character
according to the size provided, the size being the size
of the width of the square.
"""


def print_square(size):
    """This function prints a square
    Args:
        size (int): The size of the square.
    Returns:
        None
    """
    if not isinstance(size, int):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
