#!/usr/bin/python3
"""This module defines the function ``pascal_triangle``
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing the Pascal's
    triangle of ``n``
    """

    pascal = list()

    if n <= 0:
        return pascal
    if n == 1:
        return [[1]]
    else:
        pascal.append([1])

    for row in range(1, n):
        new_row = list()

        for col in range(row + 1):
            left = 0
            right = 0

            if col == 0:
                left = 0
            else:
                left = pascal[row - 1][col - 1]

            if col == row:
                right = 0
            else:
                right = pascal[row - 1][col]

            new_row.append(left + right)

        pascal.append(new_row)

    return pascal
