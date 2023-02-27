#!/usr/bin/python3
"""This module defines the function ``to_json_string``
"""

import json


def to_json_string(my_obj):
    """Returns the JSON(JavaScript Object Notation) representation
    of an object(string)
    """

    val = json.dumps(my_obj)

    return val
