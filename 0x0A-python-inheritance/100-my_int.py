#!/usr/bin/python3
"""
This module defines the class `MyInt`, a subclass of `int`
"""


class MyInt(int):
    """
    Definition of the class
    """

    def __ne__(self, value, /):
        """
        Inversion of the magic method `__eq__'
        """
        return super().__eq__(value)

    def __eq__(self, value, /):
        """
        Inversion of the magic method '__ne__'
        """
        return super().__ne__(value)
