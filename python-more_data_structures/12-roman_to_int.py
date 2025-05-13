#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    sum = 0
    found_I = False
    for s in roman_string:
        if s == 'I':
            found_I = True
        elif (s == 'V' or s == 'X') and found_I:
            sum = sum - 2
            found_I = False
        else:
            found_I = False
        sum = sum + roman.get(s)
    return sum
