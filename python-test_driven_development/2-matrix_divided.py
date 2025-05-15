#!/usr/bin/python3
"""
Provides a function matrix_divided divid all element of a matrix
"""


def matrix_divided(matrix, div):
    """
    this function divid all the element of the matrix
    """

    er_message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(er_message)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    col_len = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(er_message)
        if len(row) != col_len:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(er_message)
    new_mattrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_mattrix
