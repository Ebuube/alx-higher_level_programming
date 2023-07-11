#!/usr/bin/python3
"""
This module implements the read_file function
"""


def read_file(filename=""):
    """
    Read a text file and print it to stdout
    """
    mode = 'r'
    enc = "utf-8"
    if filename == "":
        return
    with open(filename, mode, encoding=enc) as f:
        for line in f:
            print(line, end='')
