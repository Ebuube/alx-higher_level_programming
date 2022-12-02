#!/usr/bin/python3
"""A function that checks for lowercase character."""


def islower(c):
    try:
        c = ord(c)
    except TypeError:
        sys.exit(1)

    if c >= 97 and c <= 122:
        value = True
    else:
        value = False
    return (value)
# end of function
