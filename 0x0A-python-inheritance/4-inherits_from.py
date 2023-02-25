#!/usr/bin/python3
""""Contains a method that checks for subclasses
"""


def inherits_from(obj, a_class):
    """Return True if obj is a subclass of a_class
    """

    if type(obj).__name__ == a_class.__name__:
        return False

    if issubclass(type(obj), a_class):
        return True
    else:
        return False
