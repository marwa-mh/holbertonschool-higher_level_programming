#!/usr/bin/python3
i = 122
while i >= 97:
    if i % 2 == 1:
        c = i - 32
    else:
        c = i
    print(chr(c).format(), end="")
    i = i - 1
