#!/usr/bin/python3
"""
A function to print a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    count1 = 0
    while count1 < len(matrix):
        count2 = 0
        if (len(matrix[count1]) != 0):
            while count2 < (len(matrix[count1]) - 1):
                print("{:d}".format(matrix[count1][count2]), end=' ')
                count2 += 1
            print("{:d}".format(matrix[count1][count2]))
        count1 += 1
    if (count1 == 1) and (count2 == 0):    # empty matrix
        print()
