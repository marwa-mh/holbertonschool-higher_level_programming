#!/usr/bin/python3
"""Module contain a function is_kind_of_class"""


def inherits_from(obj, a_class):
    """
    check if the obj is same type of aclass or
    from the inherited class
    """
    if isinstance(obj, a_class) and not type(obj).__name__ == a_class.__name__:
        return True
    return False
