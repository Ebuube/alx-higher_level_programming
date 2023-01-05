#!/usr/bin/python3
"""This module contains a function that is capable of manipulating a matrix.

Attributes:
    matrix_divided (def): a function calculate a matrix
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements divided by div

    All elements of the matrix is divided by ``div`` and rounded to
    2 decimal places
    Args:
        matrix (list of lists of integers or floats): first argument
        div (integer or float): number to divided all elements of matrix

    Returns:
        a new matrix which is the same as the argument matrix, but with
        all its elements divided by div

    Note:
        * matrix must be a list of lists of integers or floats, otherwise
        a TypeError exception is raised
        * Each row of the matrix must be of the same size, otherwise
        a TypeError exception is raised
        * div must be an integer or float, otherwise a TypeError
        exception is raised
        * div can't be equal to zero, otherwise a ZeroDivisionError
        exception is raised

    Usage:

        >>> matrix = [
        ...     [4, 6, 7],
        ...     [9, 10, 1],
        ...     [0, -5, -1]
        ... ]
        >>> div = 3
        >>> result = matrix_divided(matrix, div)
        >>> result == [
        ... [1.33, 2.00, 2.33],
        ... [3.00, 3.33, 0.33],
        ... [0.00, -1.67, -0.33]
        ... ]
        True
    """

    new_matrix = list()
    first_pass = False  # show whether it's the first time going trough list
    row_len = int()

    # Exception messages
    matrix_err_type = str(
        'matrix must be a matrix (list of lists)' +
        ' of integers/floats'
    )
    matrix_err_size = 'Each row of the matrix must have the same size'
    div_err_type = 'div must be a number'
    div_err_zero = 'division by zero'

    if not isinstance(matrix, list):
        raise TypeError(matrix_err_type)
    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError(div_err_type)
    if div == 0:
        raise ZeroDivisionError(div_err_zero)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_err_type)
        if first_pass is False:
            row_len = len(row)
            first_pass = True
        else:
            if len(row) != row_len:
                raise TypeError(matrix_err_size)

        new_row = list()
        for element in row:
            if ((not isinstance(element, int)) and
                    (not isinstance(element, float))):
                raise TypeError(matrix_err_type)
            else:
                result = round((element / div), 2)
                new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
