#!/usr/bin/python3
"""Module that reads text file and prints it to the stdout."""


def read_file(filename=""):
    """Reads a text file and prints it to the stdout.
    :param filename: file name of the file to read.
    """
    if not filename:
        return
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
    f.close()
