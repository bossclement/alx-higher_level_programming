#!/usr/bin/python3
"""Module that represents a student."""


class Student:
    """Blue print of a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves attributes of student."""
        return self.__dict__
