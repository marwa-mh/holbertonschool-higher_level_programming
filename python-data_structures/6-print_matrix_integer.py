#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        format_string = " ".join('{:d}'.format(x) for x in row)
        print(format_string)
    