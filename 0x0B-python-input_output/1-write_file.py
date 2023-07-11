#!/usr/python3
"""
This module implements the `write_file` function
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    Return: the number of characters written
    """
    if filename == "":
        return

    mode = 'w'      # write mode
    enc = "utf-8"   # UTF8 encoding
    with open(filename, mode, encoding=enc) as f:
        return f.write(text)
