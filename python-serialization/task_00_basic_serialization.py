#!/usr/bin/python3
"""Module contains 2 functions
serialize_and_save_to_file
load_and_deserialize"""
import pickle


def serialize_and_save_to_file(data, filename):
    """serialize the object and save it to file"""
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """deserialize data from file and return"""
    with open(filename, "rb") as file:
        data = pickle.load(file)
    return data
