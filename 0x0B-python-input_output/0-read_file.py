#!/usr/bin/python3
"""This module defines a function ``read_file()``
"""


def read_file(filename=""):
    """Read a text file and print it to stdout
    """

    with open(filename, mode="r", encoding="utf-8") as myFile:
        while True:
            line = myFile.read()
            if line == "":
                break
            else:
                print(line, end="")
