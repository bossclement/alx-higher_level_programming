#!/usr/bin/python3
"""Docs for my module goes here"""


def lookup(obj):
    """Returns list of object attributes
    Args:
        obj: the object to get attributes from.
    Returns:
        list: attributes of the obj.
    """
    return dir(obj)
