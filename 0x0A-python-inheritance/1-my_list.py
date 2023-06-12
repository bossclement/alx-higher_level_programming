#!/usr/bin/python3
"""Docs for my module goes here"""


class MyList(list):
    """Docs for my class goes here"""

    def print_sorted(self):
        i = [
            int(x) for x in map(lambda x: x.replace("[", "").
                                replace("]", "").strip(),
                                self.__str__().split(',')) if x.isnumeric()
        ]
        i.sort()
        print(i)
