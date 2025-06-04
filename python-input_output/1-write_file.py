#!/usr/bin/python3
"""function write text to file """


def write_file(filename="", text=""):
    """
    function write text to file
    """
    with open(filename, 'w') as f:
        num_of_chr = f.write(text)
    return num_of_chr
