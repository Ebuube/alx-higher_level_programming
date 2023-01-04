#!/usr/bin/python3
"""This module contains a function that adds 2 integers

Attriutes:
    add_integer (def): adds two(2) integers
"""

def add_integer(a, b=98):
    """Add two integers

    Args:
        a (int or float): first number
        b (int or float): second number an optional argument with
                            default value of 98

    Returns:
        An integer which is the sum of a and b

    Usage:
        >>> add_integer(2, 8)
        10

        On missing the second argument which is optional,
        the default value of 98 is used in its place

        >>> add_integer(5)
        103

    Note:
        A  TypeError is raised if the arguments are of any other types
        than integer or float
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
