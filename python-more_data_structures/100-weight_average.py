#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0.0
    weight = sum(x[1] for x in my_list)
    mul = sum(x[0] * x[1] for x in my_list)
    return mul / weight
