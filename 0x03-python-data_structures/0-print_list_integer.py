#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if not my_list:
        return
    print("{}".format(my_list[0]))
    my_list.pop(0)
    print_list_integer(my_list)
