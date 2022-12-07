#!/usr/bin/python3
"""
A function that finds all mulitples of 2 in a list
Returns a new list with True or False, depending on whether
the integer at the same position in the original list is a multiple
of 2
"""


def divisible_by_2(my_list=[]):
    if (my_list is None) or (len(my_list) == 0):
        return None
    new_list = list()
    for num in my_list:
        if (num % 2 == 0):    # Divisible by 2
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
