#!/usr/bin/python3
"""
Module contain a class MyList
"""


class MyList(list):
    """
    contain instance function print_sorted
    """
    def print_sorted(self):
        print(sorted(self))
