#!/usr/bin/python3
"""
Function that divides all elements of a matrix
Returns new matrix
works with a matrix(list of lists) of integers/floats
"""


def matrix_divided(matrix, div):
    """matrix divided to integer, not float
    not zero
    """
    new_matrix = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(msg)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(msg)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(msg)
        new_matrix += [list(map(lambda x: round(x/div, 2), i))]
    return new_matrix
