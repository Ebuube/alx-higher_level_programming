#!/usr/bin/python3
"""
A function that deletes the item at a specific position in a list
"""


def delete_at(my_list=[], idx=0):
    if ((idx < 0) or idx >= len(my_list)) or (len(my_list) == 0):
        return (my_list)
    if (my_list is None):
        return (None)
    del my_list[idx]
    return (my_list)
