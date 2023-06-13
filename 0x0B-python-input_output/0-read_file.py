#!/usr/bin/python3
"""Module that reads text file and prints it to the stdout."""


def read_file(filename=""):
    """Reads a text file and prints it to the stdout.
    :param filename: file name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(file.read())
    f.close()
