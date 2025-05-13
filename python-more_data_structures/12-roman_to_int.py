#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(roman_string) - 1, -1, -2):
        if i == 0:
            return sum + roman.get(roman_string[i])
        if roman.get(roman_string[i-1]) >= roman.get(roman_string[i]):
            sum += roman.get(roman_string[i - 1]) + roman.get(roman_string[i])
        else:
            sum += roman.get(roman_string[i]) - roman.get(roman_string[i - 1])
    return sum
