#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    print("{:d}".format(my_list[-1]))
    my_list.pop(-1)
    print_reversed_list_integer(my_list)
