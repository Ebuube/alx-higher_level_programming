#!/usr/bin/python3
"""This module contains the definition of some class(es)
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Define the class
    """

    def __init__(self, size):
        """Initialize a ``Square`` object
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of a ``Square`` object
        """

        return (self.__size ** 2)

    def __str__(self):
        """Return a string representation of the object
        """

        return ("[{}] {}/{}".format(type(self).__name__, self.__size,
                self.__size))
