#!/usr/bin/python3
"""
This module defines the class `BaseGeometry`
"""


class BaseGeometry:
    """
    Definition of the class
    """
    def area(self):
        """
        Raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate `value`.
        Must be an integer greater than zero(0)
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
