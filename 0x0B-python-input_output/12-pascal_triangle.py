#!/usr/bin/python3
"""
This module implements the `pascal_triangle` function
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal's triangle
    of size (n)

    Return:
        If n <= 0 then -> [[]]   # an empty list of lists
        Else: return list of list representing the Pascal's triangle of size n

    Example;
    >>> pascal_triangle(0)
    [[]]
    >>> pascal_triangle(1)
    [[1]]
    >>> pascal_triangle(2)      # doctest: +NORMALIZE_WHITESPACE
    [[1], [1, 1]]
    >>> pascal_triangle(3)      # doctest: +NORMALIZE_WHITESPACE
    [[1], [1, 1], [1, 2, 1]]
    """
    master = []     # master triangle

    # n is less than or equal to zero (0)
    if n <= 0:
        return master

    for r in range(0, n):
        if r == 0:  # for first list
            new = [1]
            master.append(new)
            continue    # compute next list
        else:
            prev = master[r - 1]    # get previous list

        # Create a new list by looking at the previous one
        new = list()
        for c in range(0, len(prev)):
            if c == 0:  # first element
                item = prev[0]
            else:
                item = prev[c - 1] + prev[c]
            # add new item to new list
            new.append(item)

        # Add last element
        new.append(prev[-1])
        # insert new list
        master.append(new)

    return master
