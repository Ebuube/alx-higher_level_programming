#!/usr/bin/python3
"""This module contains the definition of the class ``BaseGeometry``
"""


class BaseGeometry:
    """Define the class
    """

    def area(self):
        """Raise an exception with a message
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
