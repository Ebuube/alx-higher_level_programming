#!/usr/python3
"""
This module implements the `write_file` function
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    Return: the number of characters written
    """
    mode = 'w'      # write mode
    enc = "utf-8"   # UTF8 encoding
    num_chars = 0
    with open(filename, mode, encoding=enc) as f:
        num_chars = f.write(text)
        return num_chars
