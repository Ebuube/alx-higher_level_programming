#!/usr/bin/python3
"""
This module defines the is_same_class() function
"""


def is_same_class(obj, a_class):
    """
    Return `True` if `obj` is exactly an instance of `a_class` class
    """
    return (type(obj) == a_class)
