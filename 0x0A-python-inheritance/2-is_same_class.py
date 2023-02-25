#!/usr/bin/python3
"""This module contains a method that analyses an object

Attributes:
    def is_same_class(obj, a_class): Checks if ``obj`` is an instance of
    ``a_class``
"""


def is_same_class(obj, a_class):
    """Checks if ``obj`` is an instance of ``a_class``
    """

    if type(obj).__name__ == a_class.__name__:
        return True
    else:
        return False
