#!/usr/bin/python3
"""
This module has a function "matrix_divided" which
divides all elements of a matrix with a given number
and return a new matrix each element in the matrix
having 2 decimal places only.
"""


def matrix_divided(matrix, div):
    """Divides matrix with a provided divider
    Args:
        matrix (list): the matrix.
        div (int): the devider.
    Returns:
        (list): new matrix
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
