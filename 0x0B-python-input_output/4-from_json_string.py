#!/usr/bin/python3
"""
This module implements the `from_json_string` function
"""
import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string
    """
    val = json.loads(my_str)

    return val
