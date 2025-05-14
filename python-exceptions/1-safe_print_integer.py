#!/usr/bin/python3
def safe_print_integer(value):
    try:
        d = int(value)
        print("{:d}".format(d))
        return True
    except (ValueError, TypeError):
        return False
