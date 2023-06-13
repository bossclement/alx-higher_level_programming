#!/usr/bin/python3
"""Modules returns json represantation of an object."""


import json


def to_json_string(my_obj):
    """Changes a python dictionary to a string."""
    return json.dumps(my_obj)
