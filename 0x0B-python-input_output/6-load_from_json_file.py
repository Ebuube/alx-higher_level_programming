#!/usr/bin/python3
"""This module defines the function ``load_from_json_file``
"""


import json


def load_from_json_file(filename):
    """create an object from a ``JSON file``
    """

    with open(filename, mode="r", encoding="utf-8") as myFile:
        return json.load(myFile)
