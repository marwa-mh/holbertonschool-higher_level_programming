#!/usr/bin/python3
""" module contain a function to solve pascal triangle"""


def calculate_row(arr: list):
    row = [1]
    for i in range(1, len(arr) + 1):
        if i > len(arr) - 1:
            row.append(1)
            break
        row.append(arr[i] + arr[i - 1])
    return row


def pascal_triangle(n):
    result: list = []
    if n <= 0:
        return result
    result = [[1]]
    for i in range(1, n):
        row = calculate_row(result[i - 1])
        result.append(row)
    return result
