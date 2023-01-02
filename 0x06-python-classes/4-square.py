#!/usr/bin/python3
"""Module for Square class

This module contains the implementation of the class Square

Attributes:
    Square (class): Definition of the Square Class
"""


class Square:
    """Implementation of the class Square

    Attributes:
        __size: size of a side of the square represented
    """

    def __init__(self, size=0):
        """Initialize a Square object

        Args:
            size (int): size of a side of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square

        Returns:
            The area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieve the value of the object's size

        Returns:
            The value of of the object's size
        """
        return (self.__size)

    @size.setter
    def size(self, size=0):
        """Set the value of the object's size

        Args:
            size (int): size of a side of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must  be >= 0")
        else:
            self.__size = size
