#!/usr/bin/python3
sp = ""
for i in range(0, 9):
    for j in range(i+1, 10):
        print(f"{sp}{i}{j}".format(sp, i, j), end="")
        sp = ", "
print('\n')
