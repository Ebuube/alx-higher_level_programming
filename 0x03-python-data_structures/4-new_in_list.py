#!/usr/bin/python3
"""
A function that replaces an element in a list at a specific position
without modifying the original list (like in C)
"""


def new_in_list(my_list, idx, element):
    if my_list != list(my_list):
        return None
    if (idx < 0 or idx > len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return (my_list)
