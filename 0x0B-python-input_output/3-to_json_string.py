#!/usr/bin/python3
"""
This module implements the `to_json_string` function
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string)
    """
    val = json.dumps(my_obj)
    return val
