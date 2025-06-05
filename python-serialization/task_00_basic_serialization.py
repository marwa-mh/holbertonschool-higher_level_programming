#!/usr/bin/python3
"""Module contains 2 functions
serialize_and_save_to_file
load_and_deserialize"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize the object and save it to file"""
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """deserialize data from file and return"""
    with open(filename, "r") as file:
        data = json.load(file)
    return data
