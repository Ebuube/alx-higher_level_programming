#!/usr/bin/python3
"""This module contains a function that multiplies matrices

matrix_mul (def): multiplies two matrices together
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    """

    # Error messages

    def err_list(x=str()):
        """Return error message including the argument in the message
        """

        return "{} must be a list".format(str(x))

    def err_list_of_lists(x=str()):
        """Return error message including the argument in the message
        """

        return "{} must be a list of lists".format(str(x))

    def err_empty(x=str()):
        """Return error message including the argument in the message
        """

        return "{} can't be empty".format(str(x))

    def err_not_int_float(x=str()):
        """Return error message including the argument in the message
        """

        return "{} should contain only integers or floats".format(str(x))

    def err_unequal_row(x=str()):
        """Return error message including the argument in the message
        """

        return "each row of {} must be of the same size".format(str(x))

    def err_incompatible(x=str(), y=str()):
        """Return error message including the argument in the message
        """

        return "{} and {} can't be multiplied".format(str(x), str(y))

    # Validate that both arguments are lists
    if (not isinstance(m_a, list)):
        raise TypeError(err_list("m_a"))

    if (not isinstance(m_b, list)):
        raise TypeError(err_list("m_b"))

    # Validate that both arguments are list of lists
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError(err_list_of_lists("m_a"))

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError(err_list_of_lists("m_b"))

    # Validate that both arguments are not emtpy
    if (len(m_a) == 0) or (len(m_a[0]) == 0):
        raise ValueError(err_empty("m_a"))

    if (len(m_b) == 0) or (len(m_b[0]) == 0):
        raise ValueError(err_empty("m_b"))

    # Validate that both argument are lists of lists of integers/floats
    for row in m_a:
        for element in row:
            if ((not isinstance(element, int)) and
                    (not isinstance(element, float))):
                raise TypeError(err_not_int_float("m_a"))

    for row in m_b:
        for element in row:
            if ((not isinstance(element, int)) and
                    (not isinstance(element, float))):
                raise TypeError(err_not_int_float("m_b"))

    # Validate each argument is a rectangle
    # That is, each argument has rows of equal lengths
    m_a_row_len = -1
    for row in m_a:
        if m_a_row_len == -1:
            m_a_row_len = len(row)
        elif len(row) != m_a_row_len:
            raise TypeError(err_unequal_row("m_a"))

    m_b_row_len = -1
    for row in m_b:
        if m_b_row_len == -1:
            m_b_row_len = len(row)
        elif len(row) != m_b_row_len:
            raise TypeError(err_unequal_row("m_b"))

    # Validate that both arguments can be multiplied
    if (len(m_a[0]) != len(m_b)):
        raise ValueError(err_incompatible("m_a", "m_b"))

    # Multiply both matrices
    result_matrix = []
    for row in range(len(m_a)):
        new_row = []
        for col in range(len(m_b[0])):
            sum_product = 0
            for step in range(len(m_b)):
                sum_product += m_a[row][step] * m_b[step][col]
            new_row.append(sum_product)
        result_matrix.append(new_row)

    return (result_matrix)
