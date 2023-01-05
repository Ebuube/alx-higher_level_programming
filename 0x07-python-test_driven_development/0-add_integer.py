#!/usr/bin/python3
"""This module contains a function that adds 2 integers

Attriutes:
    add_integer (def): adds two(2) integers
"""


def add_integer(a, b=98):
    """Return the sum of two integers
        A TypeError is raised if the arguments are not integer or float
    """

    if isinstance(a, int) or isinstance(a, float):
        pass
    else:
        raise TypeError('a must be an integer')
    if isinstance(b, int) or isinstance(b, float):
        pass
    else:
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return (a + b)
