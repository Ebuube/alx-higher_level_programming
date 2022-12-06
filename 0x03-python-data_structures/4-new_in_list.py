#!/usr/bin/python3
"""
A function that replaces an element in a list at a specific position
without modifying the original list (like in C)
"""


def new_in_list(my_list, idx, element):
    if my_list != list(my_list):
        return None
    cp_list = my_list
    if (idx < 0 or idx > len(cp_list) - 1):
        return cp_list
    cp_list[idx] = element
    return (cp_list)
