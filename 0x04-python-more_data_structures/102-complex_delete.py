#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in a_dictionary.keys():
        key_value = a_dictionary[key]
        if key_value == value:
            del a_dictionary[key_value]
    return a_dictionary
