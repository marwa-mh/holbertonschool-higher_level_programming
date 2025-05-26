#!/usr/bin/python3
"""
Module contain abstract class Animal
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    abstract class contain abstract method
    """
    @abstractmethod
    def sound(self):
        ...


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
