#!/usr/bin/python3
"""This module contains a function that multiplies matrices

lazy_matrix_mul (def): multiplies two matrices together
"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    """

    # Multiply both matrices
    matrix_a = numpy.array(m_a)
    matrix_b = numpy.array(m_b)
    ans = numpy.dot(matrix_a, matrix_b)

    # Convert answer to a list of lists
    result_matrix = []
    for row in ans:
        result_matrix.append(list(row))

    return (result_matrix)
