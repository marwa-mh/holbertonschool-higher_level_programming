#!/usr/bin/python3
""" returns the dictionary description with simple data structure """


def class_to_json(obj: object):
    result: dict
    result = obj.__dict__
    result = {k: v for k, v in result.items() if k not in {'_MyClass__name'}}
    return result
