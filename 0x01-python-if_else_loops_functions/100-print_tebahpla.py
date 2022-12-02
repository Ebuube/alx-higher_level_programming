#!/usr/bin/python3
"""
A program that prints the ASCII alphabet, in reverse order, alternating
lowercase and uppercase (z in lowercase and Y in uppercase), not followed
by a new line.
"""


for char in range(0, 26):
    char = 122 - char    # reverse order
    if (char % 2 == 1):
        char = char - 32    # alternating case
    print('{}'.format(chr(char)), end='')
