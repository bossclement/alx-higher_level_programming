#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = {None: 0}
    for key, value in a_dictionary.items():
        if biggest.values()[0] < value:
            biggest = {key: value}
    return biggest.keys()[0]
