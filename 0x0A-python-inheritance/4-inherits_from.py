#!/usr/bin/python3
"""Docs for my module goes here"""


def inherits_from(obj, a_class):
    """Returns true if an object is a
    subclass of a specified class
    Args:
        obj: the object.
        a_class: the class.
    Returns:
        bool: True if yes, False if not.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
