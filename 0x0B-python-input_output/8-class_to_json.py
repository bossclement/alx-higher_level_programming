#!/usr/bin/python3
"""Returns a dictionary description of an object."""


def class_to_json(obj):
    """Returns a class dictionary description.
    Args:
        obj (any): The object to get the dictionry for.

    Returns:
        dict: Dictionary description of the object.
    """
    return obj.__dict__
