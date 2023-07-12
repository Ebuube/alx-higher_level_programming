#!/usr/bin/python3
"""
This module implements the `class_to_json` function
"""


def class_to_json(obj):
    """
    Return the dictionary description of an object
    list, string, integer or boolean
    """

    return obj.__dict__
