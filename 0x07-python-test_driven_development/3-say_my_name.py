#!/usr/bin/python3
"""
This modules has a function that prints out
the full name of a particular individual,
it takes 2 arguments, first name and last name
respectively, then prints out the full name.
"""


def say_my_name(first_name, last_name=""):
    """Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
