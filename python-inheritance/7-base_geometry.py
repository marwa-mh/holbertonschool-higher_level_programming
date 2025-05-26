#!/usr/bin/python3
"""
Module contains class BaseGeometery
                instance method : area
"""


class BaseGeometry:
    """instance method area"""
    def area(self):
        raise Exception("area() is not implemented")

    """integer_validator method"""
    def integer_validator(self, name, value):
        if not type(value).__name__ == int.__name__:
            raise TypeError(f"{name} must be an integer".format())
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0".format())
