#!/usr/bin/python3
"""
This module contain a class Rectangle
"""


class Rectangle:
    """
    This class is empty
    """
    @classmethod
    def __validate(self, width, height):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def __init__(self, width=0, height=0):
        Rectangle.__validate(width, height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate(value, 0)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate(0, value)
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        result = ""
        if self.__width <= 0:
            return result
        for i in range(self.__height):
            result = result + self.__width * '#'
            result = result + '\n' if i < (self.__height - 1) else result
        return result
