#!/usr/bin/python3
"""Module that represents a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(x=x, y=y, id=id, width=size, height=size)
        self.width = size

    def __str__(self):
        """Returns str represantation of my class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width
                                                 )

    @property
    def size(self):
        """Retrieves the value of size."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of my class."""
        attributes = ["id", "size", "x", "y"]
        assigned = []
        for index, arg in enumerate(args):
            if index >= len(attributes):
                break
            assigned.append(attributes[index])
            setattr(self, attributes[index], arg)

        not_assigned = set(list(kwargs.keys())).difference(set(assigned))
        for attr in not_assigned:
            setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """Returns certain attributes of my class."""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.width}

    def to_csv_row(self):
        """Converts class object to csv file."""
        result = ''
        for value in [self.id, self.width, self.height, self.x, self.y]:
            value = value if type(value) == int else ''
            result += "{},".format(value)
        return result[:-1]

    @classmethod
    def from_csv_row(cls, row):
        """Cinverts a csv row to a python object"""
        while ',' in row:
            row.remove(",")
        data = list(map(lambda x: int(x) if x.isnumeric() else None, row))
        return cls(data[1], data[2], data[3], data[0])
