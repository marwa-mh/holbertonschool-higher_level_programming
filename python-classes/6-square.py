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
        if not isinstance(position, tuple) or not all(isinstance(e,int) for e in position) or not len(position) == 2 or len(list(x for x in position if x < 0)) > 0:
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
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            any(n < 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        printed:bool = False
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
        """for r in range(self.size):
            if self.position[0] > 0:
                    for k in range(self.position[0]):
                        print("_", end="")
            for c in range(self.size):               
                print("#", end="")
            print()
"""