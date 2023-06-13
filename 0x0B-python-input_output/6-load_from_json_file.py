#!/usr/bin/python3
"""Loads a python object from a file."""


import json


def load_from_json_file(filename):
    """Loads json file into a python dictionary.
    Args:
        filename (str): file path of the json file.

    Returns:
        dict: Returns a python dictionary.
    """

    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
