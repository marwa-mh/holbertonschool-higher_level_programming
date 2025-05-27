#!/usr/bin/python3
"""
Module contain a class VerboseList
"""


class VerboseList(list):
    def append(self, object):
        super().append(object)
        print(f"Added [{object}] to the list.".format())
        return super()

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.".format())

    def pop(self, index=-1):
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        return super().remove(value)
