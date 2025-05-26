#!/usr/bin/python3
"""Module contain a function is_same_class"""


def is_same_class(obj, a_class):
    """
    check if the obj is same type of aclass
    """
    if isinstance(type(obj), a_class):
        return True
    return False
