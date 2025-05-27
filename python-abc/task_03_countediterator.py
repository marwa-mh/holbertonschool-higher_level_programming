#!/usr/bin/python3
"""
Module contain class CountedIterator
"""


class CountedIterator:
    def __init__(self, some_iterable):
        self.__counter = 0
        self.iterator = iter(some_iterable)

    def get_count(self):
        return self.__counter

    def __next__(self):
        self.__counter += 1
        return self.iterator.__next__()
