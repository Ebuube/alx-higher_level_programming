#!/usr/bin/python3
"""This module contains a function that prints a square with the character
``#``

Attributes:
    print_square (def): prints a square using the character ``#``
"""


def print_square(size):
    """Print a square using the character ``#``

    Args:
        size (int): size length of the square

    Note:
        If size is less than 0, a ValueError is raised
        If size is zero(0), an empty line is printed

    Usage:
        >>> print_square(4)
        ####
        ####
        ####
        ####
    """

    if (not isinstance(size, int)):
        raise TypeError('size must be an integer')
    if not (size >= 0):
        raise ValueError('size must be >= 0')

    if size == 0:
        print()
    else:
        for y_len in range(size):
            for x_len in range(size):
                print('#', end="")
            print()
