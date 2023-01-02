#!/usr/bin/python3
"""A module for the class Square

This module contains capable class for representing a Square object
"""


class Square:
    """class Square

    This class contains capable methods for manipulating a Square object

    Attributes:
        __size (int): size of the square instance
    """

    def __init__(self, size=0):
        """method __init__

        This method initializes an instance of the class Square

        Args:
            size (int): represents the size of a Square object
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
