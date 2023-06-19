#!/usr/bin/python3
"""Will have the base class for other classes for my project"""
import json


class Base:
    """The base class for my project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor function for my project."""

        if not id:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """returns json string"""
        if not list_dictionaries:
            return '"[]"'
        return json.dumps(list_dictionaries)
