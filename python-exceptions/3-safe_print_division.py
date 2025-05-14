#!/usr/bin/python3
def safe_print_division(a, b):
    result = ""
    try:
        x = a / b
        result = "{}".format(a / b)
    except (ValueError, TypeError, ZeroDivisionError):
        result = "None"
    finally:
        print(f"Inside result: {result}")
        return result
