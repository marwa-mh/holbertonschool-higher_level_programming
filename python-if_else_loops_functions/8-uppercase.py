#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    for c in str:
        print(chr(ord(c) - 32) if islower(c) else c, end="")
    print()
