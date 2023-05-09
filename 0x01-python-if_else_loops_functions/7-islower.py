#!/usr/bin/python3
def islower(c):
    if isinstance(c, str):
        return ord(c) > 96 and ord(c) < 123
    return False
