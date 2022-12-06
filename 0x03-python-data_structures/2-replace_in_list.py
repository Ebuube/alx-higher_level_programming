#!/usr/bin/python3
"""
A function that replaces an element of a list at a specified position
like in C
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return (my_list)
