#!/usr/bin/python3
"""
Module contain a class MyList
"""


class MyList(list):
    """
    contain instance function print_sorted
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
