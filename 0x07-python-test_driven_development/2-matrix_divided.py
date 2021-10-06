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
    """if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) is ???? 
        raise TypeError("Each row of the matrix must have the same size") """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")	
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix += [list(map(lambda x: round(x/div, 2), i))]
    return new_matrix
