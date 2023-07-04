#!/usr/bin/python3
def magic_calculation(a, b, c):
    if (a < b) is False:
        if (c > b) is False:
            return (a * b) - c
        else:
            return a + b
    else:
        return c
