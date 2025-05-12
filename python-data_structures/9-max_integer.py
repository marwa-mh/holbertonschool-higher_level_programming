#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_number = my_list[0]
    for n in my_list[1:]:
        max_number = n if max_number < n else max_number
    return max_number
