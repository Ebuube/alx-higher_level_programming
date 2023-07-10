#!/usr/bin/python3
"""
This module defines the class `Square`, subclass of `Rectangle`
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Definition of the class
    """
    def __init__(self, size):
        """
        Initialization of instance
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """
        Return the size of the instance raised to power 2
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the non-canonical string representation of instance
        """
        val = "[{}] {}/{}".format(type(self).__name__,
                                  self.__size, self.__size)
        return val
