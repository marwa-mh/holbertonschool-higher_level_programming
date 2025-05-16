#!/usr/bin/python3
"""
this module provide a function text_indentation
"""


def text_indentation(text):
    """
    this function print a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while (i < len(text)):
        if text[i] in ('.', ':', '?'):
            result = result + '\n\n'
            i = i + 1
            while (text[i] == ' '):
                i += 1
        else:
            result += text[i]
            i += 1
    print(result)
