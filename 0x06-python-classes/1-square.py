#!/usr/bin/python3
"""A module that defines the class Square

This module contains the implementation of the class Square
"""


class Square:
    """Defines a Square object

    This class has attributes of a square and functions for manipulating
    and extracting information from them
    """

    def __init__(self, size):
        """initialize the square with the value, size

        Args:
            size (numerical): a numerical data type
        """
        self.__size = size
