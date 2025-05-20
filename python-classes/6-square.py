#!/usr/bin/python3
"""
this module provides a square class
"""


class Square:
    """
    contain a function __init__
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        condition = not isinstance(position, tuple)
        condition = condition or not all(isinstance(e, int) for e in position)
        condition = condition or not len(position) == 2
        if condition or len(list(x for x in position if x < 0)) > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        condition = not isinstance(value, tuple)
        condition = condition or len(value) != 2
        condition = condition or not all(isinstance(n, int) for n in value)
        condition = condition or any(n < 0 for n in value)
        if condition:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.size == 0:
            print()
            return
        for x in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
