#!/usr/bin/python3
"""This moduule defines the funciton ``from_json_string``
"""


import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON
    object
    """

    return json.loads(my_str)
