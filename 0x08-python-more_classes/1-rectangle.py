#!/usr/bin/python3
"""This module contains the definition of a class ``Rectangle``
"""


class Rectangle:
    """Defines the class ``Rectangle``
    """

    def __init__(self, width=0, height=0):
        """
        Initialization of an instance
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieve the width attribute of a Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of the 'width' attribute
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height attribute of a Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of the 'height' attribute of a Rectangle
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value
