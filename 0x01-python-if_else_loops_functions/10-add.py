#!/usr/bin/python3
"""
A function that adds two integers and returns the result
"""


def add(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        exit(1)

    return (a + b)
# end of function
