#!/usr/bin/python3
"""Writes a python object to a file."""


import json

def save_to_json_file(my_obj, filename):
    """Saves an object to a file.
    :param my_obj: Python object (dict).
    :param filename: File name where to save the object.
    """

    with open(filename, mode="w+", encoding="utf-8") as f:
        json.dump(my_obj, f)
    f.close()
