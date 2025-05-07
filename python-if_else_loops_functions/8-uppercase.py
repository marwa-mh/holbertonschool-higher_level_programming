#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False

def uppercase(str):
    for c in str:
        print(chr(ord(c) - 32) if islower(c) else c, end="")
    print()
