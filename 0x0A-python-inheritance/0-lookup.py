#!/usr/bin/python3
"""
This module defines the lookup method
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object
    """
    return (list(obj.__dict__))
