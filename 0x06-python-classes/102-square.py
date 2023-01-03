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

    def __eq__(self, obj_square):
        """Define `equal to` comparision operator overloader

        Raises a TypeError if argument is not a Square object

        Returns:
            True if this object and argument have the same size
            else False
        """
        if not isinstance(obj_square, Square):
            raise TypeError("argument must be a Square object")
        else:
            return (self.__size == obj_square.size)

    def __ne__(self, obj_square):
        """Define `not equal` comparison operator overloader

        Raises a TypeError if argument is not a Square object

        Returns:
            True if this object and the argument have different sizes
            else False
        """

        if not isinstance(obj_square, Square):
            raise TypeError("argument must be a Square object")
        else:
            return (self.__size != obj_square.size)

    def __gt__(self, obj_square):
        """Define `greater than` comparison operator overloader

        Raises a TypeError if argument is not a Square object

        Returns:
            True if this object's size is greater than the argument's size
            else False
        """

        if not isinstance(obj_square, Square):
            raise TypeError("argument must be a Square object")
        else:
            return (self.__size > obj_square.size)

    def __ge__(self, obj_square):
        """Define `greater than or equal to` comparison operator overloader

        Raises a TypeError if argument is not a Square object

        Returns:
            True if this object's size is greater than or equal to
            the argument's size
            else False
        """

        if not isinstance(obj_square, Square):
            raise TypeError("argument must be a Square object")
        else:
            return (self.__size >= obj_square.size)

    def __lt__(self, obj_square):
        """Define `less than` comparison operator overloader

        Raises a TypeError if argument is not a Square object

        Returns:
            True if this object's size is less than the argument's size
            else False
        """

        if not isinstance(obj_square, Square):
            raise TypeError("argument must be a Square object")
        else:
            return (self.__size < obj_square.size)

    def __le__(self, obj_square):
        """Define `less than or equal to` comparison operator overloader

        Raises a TypeError if argument is not a Square object

        Returns:
            True if this object's size is less than or eqaul to
            the argument's size
            else False
        """

        if not isinstance(obj_square, Square):
            raise TypeError("argument must be a Square object")
        else:
            return (self.__size <= obj_square.size)

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
