#!/usr/bin/python3
"""
This module defines the function `add_attribute`
"""


def add_attribute(obj, key, val):
    """
    Add a new {`key`: `value`} pair to `obj` if possible
    Else, raise TypeError
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, key, val)
    else:
        raise TypeError("can't add new attribute")
