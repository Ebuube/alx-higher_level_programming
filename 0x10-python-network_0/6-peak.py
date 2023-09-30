#!/usr/bin/python3
"""
Technical interview
NB: A peak element in a list of integers is any element that is greater
than both of its neighboring elements
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of integers
    """
    if list_of_integers is None or type(list_of_integers) is not list:
        return
    if len(list_of_integers) == 0:
        return

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
    elif len(list_of_integers) == 3:
        if (list_of_integers[1] >= list_of_integers[0] and
                list_of_integers[1] >= list_of_integers[2]):
            return list_of_integers[1]
        else:
            return None
    else:
        mid = len(list_of_integers) / 2
        n_int = int(mid)
        if mid > n_int:
            mid = n_int + 1
        else:
            mid = n_int

        left = find_peak(list_of_integers[:mid])
        right = find_peak(list_of_integers[mid:])
        if (left is not None) and (left > right):
            return left
        else:
            return right
