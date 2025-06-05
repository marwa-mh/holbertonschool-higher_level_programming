#!/usr/bin/python3
""" module contain class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        rslt: dict
        rslt = self.__dict__
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            rslt = {k: v for k, v in rslt.items() if k  in {item for item in attrs}}
        else:
            rslt = {k: v for k, v in rslt.items() if k not in {'_MyClass__name'}}
        return rslt
