#!/usr/bin/python3
"""Inserts a line of text inside a file."""


def append_after(filename="", search_string="", new_string=""):
    """Appends a text in a file after each line containing
    a search keyword.
    """
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        f.close()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.write("\n")
