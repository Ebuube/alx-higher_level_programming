#!/usr/bin/python3
"""
This module implements the `append_write` function
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8)
    Return:
        the number of characters added
    """
    num_chars = 0
    if filename != "":
        mode = 'a'
        enc = "utf-8"
        with open(filename, mode, encoding=enc) as f:
            num_chars = f.write(text)

    return num_chars
