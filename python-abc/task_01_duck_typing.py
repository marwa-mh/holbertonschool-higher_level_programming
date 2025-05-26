#!/usr/bin/python3
"""
Module contain abstract class Animal
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    abstract class contain abstract method
    """
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * math.pow(self.__radius, 2)

    def perimeter(self):
        return 2 * math.pi * abs(self.__radius)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2


def shape_info(obj: Shape):
    print(f"Area: {obj.area()}".format())
    print(f"Perimeter: {obj.perimeter()}")
