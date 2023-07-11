#!/usr/bin/python3
"""
This module implements the `load_from_json_file` function
"""
import json


def load_from_json_file(filename):
    """
    Create an object from a "JSON file"
    """
    obj = None
    if filename != "":
        mode = 'r'
        enc = "utf-8"
        with open(filename, mode, encoding=enc) as f:
            obj = json.load(f)

    return obj
