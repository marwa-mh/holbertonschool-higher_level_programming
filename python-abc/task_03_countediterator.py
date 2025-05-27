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
        next_item = next(self.iterator, None)
        if next_item is None:
            print("finish")
            raise StopIteration()
        self.__counter += 1
        return next_item
