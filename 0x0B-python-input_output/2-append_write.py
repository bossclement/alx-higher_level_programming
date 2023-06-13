#!/usr/bin/python3
"""This module appends a string to the end of a file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a file.
    Args:
        filename (str): The file name.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters appended.
    """

    with open(filename, encoding="utf-8", mode="a") as f:
        f.write(text)
    f.close()
