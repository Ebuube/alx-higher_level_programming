#!/usr/bin/python3
"""
This module defines the `inherits_from()` function
"""


def inherits_from(obj, a_class):
    """
    Return True only if:
        * `obj` directly/indirectly inherits from `a_class` class
    Else:
        * Return False
    """
    return issubclass(type(obj), a_class) and not type(obj) is a_class
