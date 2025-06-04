#!/usr/bin/python3
"""function to append text to file """


def append_write(filename="", text=""):
    """
    function append text to file
    """
    with open(filename, 'a',  encoding="utf-8") as f:
        num_of_chr = f.write(text)
    return num_of_chr
