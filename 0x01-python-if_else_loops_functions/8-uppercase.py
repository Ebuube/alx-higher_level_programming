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


def uppercase(str):
    for count in range(len(str)):
        my_char = str[count]
        if islower(my_char):
            my_char = chr(ord(my_char) - 32)
        if count < len(str) - 1:
            print("{}".format(my_char), end='')
        else:
            print("{}".format(my_char))
# end of function

# test
