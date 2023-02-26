#!/usr/bin/python3
"""This module contains a method
"""

def add_attribute(obj, attr, val):
    """Add the attribute ``attr`` with value ``val`` to the object ``obj``
    Raises TypeError if impossible to add new attribute
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attr, val)
    else:
        raise TypeError("can\'t add new atrribute")
