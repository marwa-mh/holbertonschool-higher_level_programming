#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = sum(x[1] for x in my_list)
    mul = sum(x[0] * x[1] for x in my_list)
    return mul / weight
