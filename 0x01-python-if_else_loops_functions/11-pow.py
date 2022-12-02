#!/usr/bin/python3
"""
A function that computes a to the power b and returns the result
"""


def pow(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        exit(1)

    return (a ** b)
# end of function
