#!/usr/bin/python3
"""function write text to file """


def write_file(filename="", text=""):
    """
    function write text to file
    """
    with open(filename, encoding="utf-8") as f:
        num_of_chr = f.write(text)
        f.close()
        print(num_of_chr, end="")
