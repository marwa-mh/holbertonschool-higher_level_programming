#!/usr/bin/python3
def no_c(my_string):
    remove_chars = "cC"
    translation_table = my_string.maketrans("", "",  remove_chars)
    my_string = my_string.translate(translation_table)
    return my_string
