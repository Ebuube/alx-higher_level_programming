#!/usr/bin/python3
"""
A function that finds the biggest integer of a list
"""


def max_integer(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return (None)
    l_max = my_list[0]
    for num in my_list:
        if (l_max < num):
            l_max = num
    return (l_max)
