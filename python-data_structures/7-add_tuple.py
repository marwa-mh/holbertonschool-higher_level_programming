#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    tuple_a = tuple(list(tuple_a)[:2] + [0] * (2 - len(tuple_a)))
    tuple_b = tuple(list(tuple_b)[:2] + [0] * (2 - len(tuple_b)))
    res = tuple(map(sum, zip(tuple_a, tuple_b)))
    return res
