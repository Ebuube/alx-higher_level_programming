#!/usr/bin/python3
"""This module contains a function that returns the list of available
attributes and methods of an object

Atrributes:
    lookup(obj): list the available attributes and methods of ``obj``
"""


def lookup(obj):
    """Returns a list of available objects of ``obj``
    """

    my_list = dir(obj)

    return (my_list)
