#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for x in my_list:
        res.append(True if x % 2 == 0 else False)
    return res
