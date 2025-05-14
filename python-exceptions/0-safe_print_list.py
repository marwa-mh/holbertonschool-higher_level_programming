#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(f"{my_list[i]}".format(), end="")
        print()
    except IndexError:
        print()
    return x
