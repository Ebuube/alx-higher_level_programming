#!/usr/bin/python3
"""
A program that imports functions from the file calculator_1.py
and does some maths and prints the result.
"""


if __name__ = '__main__':
    from calculator_1 import sub, add, mul, div
    a = 10
    b = 5
    print(a, '+', b, '=', add(a, b), end=' ')
    print(a, '-', b, '=', sub(a, b), end=' ')
    print(a, '*', b, '=', mul(a, b), end=' ')
    print(a, '/', b, '=', div(a, b), end=' ')
