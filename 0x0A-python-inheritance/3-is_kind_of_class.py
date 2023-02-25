#!/usr/bin/python3
"""This module contains a method that verifies similar classes
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of, or if the object ``obj`` is an
    instance of a class that inherited from the specified class, ``a_class``
    ; otherwise False
    """

    if issubclass(type(obj), a_class):
        return True
    else:
        return False
