#!/usr/bin/python3
"""
A function that adds two tuples
"""


def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) < 1):
        a0 = 0
    else:
        a0 = tuple_a[0]
    if (len(tuple_b) < 1):
        b0 = 0
    else:
        b0 = tuple_b[0]
    if (len(tuple_a) < 2):
        a1 = 0
    else:
        a1 = tuple_a[1]
    if (len(tuple_b) < 2):
        b1 = 0
    else:
        b1 = tuple_b[1]
    tuple_c = ((a0 + b0), (a1 + b1))
    return (tuple_c)
