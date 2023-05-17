#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def mul(x):
        return x * number
    new_list = list(map(mul, my_list))
    return new_list
