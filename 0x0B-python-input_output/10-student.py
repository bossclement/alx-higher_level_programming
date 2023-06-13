#!/usr/bin/python3
"""Module that represents a student."""


class Student:
    """Blue print of a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves attributes of student."""
        attributes = self.__dict__
        result = {}
        if type(attrs) == list:
            for attr in attrs:
                if attr in attributes:
                    result.update({attr: attributes[attr]})
                elif type(attr) != str:
                    return attributes
            return result
        return attributes
