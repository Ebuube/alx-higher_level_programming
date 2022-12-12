#!/usr/bin/python3
"""
A function that computes the square value of all integers of a matrix
matix: a 2 dimensional array
Returs a new matrix:
    Same size as matrix
    Each value should be the squre of the value of the input
Initial matrix should not be modified
"""


def square_matrix_simple(matrix=[]):
    if not matrix:
        return (matrix)
    res = []
    for sub_list in matrix:
        res.append(list(map((lambda element: element ** 2), sub_list)))
    return (res)
