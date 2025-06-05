#!/usr/bin/python3
""" module contain class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        t: dict
        t = self.__dict__
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            t = {k: v for k, v in t.items() if k in {s for s in attrs}}
        else:
            t = {k: v for k, v in t.items() if k not in {'_MyClass__name'}}
        return t

    def reload_from_json(self, json):
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
