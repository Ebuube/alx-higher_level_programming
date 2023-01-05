#!/usr/bin/python3
"""This module contains a function that adds 2 integers

Attriutes:
    add_integer (def): adds two(2) integers
"""


def add_integer(a, b=98):
    """Return the sum of two integers
        A TypeError is raised if the arguments are not integer or float
    """

    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError('a must be an integer')
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError('b must be an integer')

    return int(int(a) + int(b))
