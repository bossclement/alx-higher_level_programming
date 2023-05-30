#!/usr/bin/python3

"""
Docs for module
"""


class Node:
    """class docs"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data value
        Returns:
            int: the value of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value of data"""
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the value of next_node property
        Returns:
            Node: returns a node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of next_node"""
        if not isinstance(value, Node) and \
                value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """My class"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        new = Node(value)
        cp = self.head
        prev = None
        while cp:
            if cp.data > value:
                break
            prev = cp
            cp = cp.next_node
        if prev:
            new.next_node = cp
            prev.next_node = new
        else:
            new.next_node = cp

        if self.head is None or self.head.data > new.data:
            self.head = new

    def __str__(self):
        data = ""
        cp = self.head
        while cp:
            data += "{:d}\n".format(cp.data)
            cp = cp.next_node
        return data[:-1]
