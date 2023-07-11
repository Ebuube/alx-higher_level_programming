#!/usr/bin/python3
"""
This module implements the `save_to_json_file` function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an Object `my_obj` to a text file, using JSON representation
    """
    if filename != "":
        mode = 'w'
        enc = "utf-8"
        with open(filename, mode, encoding=enc) as f:
            json.dump(my_obj, f)
