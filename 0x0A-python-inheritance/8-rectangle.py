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
