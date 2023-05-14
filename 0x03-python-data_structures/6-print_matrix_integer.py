#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for my_list in matrix:
        for index, element in enumerate(my_list):
            print("{:d}".format(element), end=" " if index < (len(my_list) - 1) else "")
        print("")
