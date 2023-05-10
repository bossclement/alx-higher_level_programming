#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for index, value in enumerate(str):
        if index != n:
            new += value
