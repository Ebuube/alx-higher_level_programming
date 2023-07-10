#!/usr/bin/python3
"""
This module defines the `is_kind_of_class()` function
"""


def is_kind_of_class(obj, a_class):
    """
    Return `True` if:
        * `obj` is an instance of `a_class`
        * `obj` is an instance of a subclass of `a_class`
    Else:
        * Return `False`
    """
    return isinstance(obj, a_class)
