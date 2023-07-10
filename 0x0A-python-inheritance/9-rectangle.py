#!/usr/bin/python3
"""
This module defines the class `Rectangle`, subclass of `BaseGeometry`
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Definition of the class
    """
    def __init__(self, width, height):
        """
        Initialization of instance
        """
        args = {'width': width, 'height': height}
        for key, val in args.items():
            self.integer_validator(key, val)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the product of the `width` and `height` of the instance
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the non-canonical string representation of instance
        """
        val = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return val
