#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    def square(num):
        return num ** 2
    for i in matrix:
        new_list.append(list(map(square, i)))
    return new_list
