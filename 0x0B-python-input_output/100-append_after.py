#!/usr/bin/python3
"""
This module implements the `append_after` function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text to a file, after each line containing
    `new_string`
    """
    if filename == "":
        return

    enc = "utf-8"   # UTF8 encoding

    # Read and update file data
    file_data = str()

    with open(filename, 'r', encoding=enc) as f:
        for line in f:
            if search_string in line:
                line = line + new_string
            file_data = file_data + line

    # Write changes to file
    with open(filename, 'w', encoding=enc) as f:
        f.write(file_data)
