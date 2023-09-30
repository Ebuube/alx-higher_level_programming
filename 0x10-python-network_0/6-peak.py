#!/usr/bin/python3
"""
Technical interview
NB: A peak element in a list of integers is any element that is greater
than both of its neighboring elements
"""


def ceil(frac):
    """
    Find the lowest number greater than the fraction
    e.g
    >>> ceil(5.5)
    6
    >>> ceil(5)
    5
    """
    if type(frac) is int:
        return frac
    if not isinstance(frac, float):
        return

    n_int = int(frac)
    if frac > n_int:
        return n_int + 1
    else:
        return n_int


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
        mid = ceil(len(list_of_integers) / 2)
        left = find_peak(list_of_integers[:mid])
        right = find_peak(list_of_integers[mid:])
        if (left is not None) and (left > right):
            return left
        else:
            return right
