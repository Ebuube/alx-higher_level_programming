#!/usr/bin/python3
"""This module defines the function ``append_write()``
"""


def append_write(filename="", text=""):
    """Appends text to a file and return the number of characters written
    """

    num_chars = 0

    with open(filename, mode="a", encoding="utf-8") as myFile:
        num_chars = myFile.write(text)

    return num_chars
