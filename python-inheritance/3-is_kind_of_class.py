#!/usr/bin/python3
"""Module contain a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    check if the obj is same type of aclass or
    from the inherited class
    """
    if isinstance(obj, a_class):
        return True
    return False
