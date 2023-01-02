#!/usr/bin/python3
"""A module for the class Square

This module contains capable class for representing a Square object
"""


class Square:
    """class Square

    This class contains capable methods for manipulating a Square object
    """

    def __init__(self, size=0):
        """method __init__

        This method initializes an instance of the class Square

        Args:
            size (int): represents the size of a Square object
        """

        if type(size) != int:
            try:
                raise TypeError
            except TypeError as e:
                print('size must be an integer')
        elif size < 0:
            try:
                raise ValueError
            except ValueError as e:
                print('size must be >= 0')
        else:
            self.__size = size
