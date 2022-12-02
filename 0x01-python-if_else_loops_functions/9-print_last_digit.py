#!/usr/bin/python3
"""
A function that prints the last digit of a number
"""


def print_last_digit(number):
    last = abs(number) % 10
    print('{}'.format(last), end='')
    return (last)
# end of function
