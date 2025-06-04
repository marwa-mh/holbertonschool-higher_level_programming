#!/usr/bin/python3
"""function reads text """


def read_file(filename=""):
    """
    function read text from file
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        f.close()
        print(read_data,end="")
