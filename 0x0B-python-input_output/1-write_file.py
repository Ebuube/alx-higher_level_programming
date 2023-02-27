#!/usr/bin/python3
"""This module defines the function ``write_file()``
"""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written
    """

    num_chars = 0

    with open(filename, mode="w", encoding="utf-8") as myFile:
        num_chars = myFile.write(text)

    return num_chars
