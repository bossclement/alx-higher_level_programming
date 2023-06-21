#!/usr/bin/python3
"""Will have the base class for other classes for my project"""
import json
import turtle
import time
from random import randrange


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

    @staticmethod
    def from_json_string(json_string):
        """Converts json string to python object."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns all attributes of a class already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)

                instances = [cls.create(**d) for d in data]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save my list objects to a csv file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:

            for obj in list_objs:
                row = obj.to_csv_row()
                file.write(row + '\n')

    @classmethod
    def load_from_file_csv(cls):
        """Loads my object instances from a csv file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                instances = []

                for row in file:
                    obj = cls.from_csv_row(row.replace('\n', '').split(","))
                    if obj:
                        instances.append(obj)

                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A static method that opens a window and draws all the instances"""

        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("violet")
        t.shape("square")
        t.pensize(8)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Draws a rectangle or a square"""

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
