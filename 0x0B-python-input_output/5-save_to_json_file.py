#!/usr/bin/python3
"""This module defines the function ``save_to_json_file``
"""

import json


def save_to_json_file(my_obj, filename):
    """Write a Object to a text file, using a JSON representation
    """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
