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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""
        if not list_dictionaries or not isinstance(list_dictionaries, list):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a json string to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as file:
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
            file.write(json_string)
