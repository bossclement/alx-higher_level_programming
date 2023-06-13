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
        last = ''
        for line in lines:
            f.write(line)
            last = line
            if search_string in line:
                last = new_string
                f.write(new_string)
        if last[-1] != '\n':
            f.write('\n')
    f.close()
