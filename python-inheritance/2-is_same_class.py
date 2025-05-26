#!/usr/bin/python3
"""Module contain a function is_same_class"""


def is_same_class(obj, a_class):
    """
    check if the obj is same type of aclass
    """
    if type(obj).__name__ == a_class.__name__:
        return True
    return False
