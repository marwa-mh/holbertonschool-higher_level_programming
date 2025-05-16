#!/usr/bin/python3
"""
this module provide a function print_square
"""


def print_square(size):
    err_mes_int = "size must be an integer"
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError(err_mes_int)
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#".format(), end="")
        print()
