#!/usr/bin/python3
"""
A function that removes all characters c and c from string.
"""


def no_c(my_string):
    new_string = str()
    count = 0
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        new_string += char
        count += 1
    return new_string
