#!/usr/bin/python3
"""Docs for my module goes here"""


def is_same_class(obj, a_class):
    """Returns true if an object is an 
    instance of a specified class
    Args:
        obj: the object.
        a_class: the class.
    Returns:
        bool: True if yes, False if not.
    """
    return issubclass(obj, a_class)
