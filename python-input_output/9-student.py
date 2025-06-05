#!/usr/bin/python3
""" module contain class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        result: dict
        result = self.__dict__
        result = {k: v for k, v in result.items()
                  if k not in {'_MyClass__name'}}
        return result
