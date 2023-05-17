#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = {}
    for key, key_value in a_dictionary.items():
        if key_value != value:
            new[key] = key_value
    return new
