#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    max_length = min(len(tuple_a), len(tuple_b))
    if max_length > 2:
        max_length = 2
    for i in range(0, max_length):
        res.append(tuple_a[i] + tuple_b[i])
    if max_length < 2:
        if len(tuple_b) > max_length:
            for i in range(max_length, 2):
                res.append(tuple_b[i])
        if len(tuple_a) > max_length:
            for i in range(max_length, 2):
                res.append(tuple_a[i])
    res = tuple(res)
    return res
