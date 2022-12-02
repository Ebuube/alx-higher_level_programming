#!/usr/bin/python3
"""
A function that creates a copy of the string, removing the character
at the postion `n` (not the python way, the "C array index").
"""


def remove_char_at(str, n):
    my_str = ""
    count = int()
    try:
        n = int(n)
    except ValueError:
        exit(1)

    for count in range(0, len(str)):
        if count == n:
            continue
        else:
            my_str += str[count]
    return (my_str)
# end of function
