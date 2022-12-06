#!/usr/bin/python3
"""
A function to print a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    if (matrix is None) or (len(matrix) == 0):
        return None
    count1, count2 = 0, 0
    for count1 in range(len(matrix)):
        for count2 in range(len(matrix[0]) - 1):
            print("{} ".format(matrix[count1][count2]), end=' ')
        print("{}".format(matrix[count1][count2 + 1]))
