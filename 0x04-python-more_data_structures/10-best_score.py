#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = {None: 0}
    if a_dictionary:
        for key, value in a_dictionary.items():
            if list(biggest.values())[0] < value:
                biggest = {key: value}
    return list(biggest.keys())[0]
