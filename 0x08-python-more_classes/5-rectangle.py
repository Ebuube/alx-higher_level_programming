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
        self.__width = 0
        self.__height = 0

        self.width = width
        self.height = height

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

    def area(self):
        """
        Return the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the rectangle perimeter
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the graphical representation of a Rectangle
        """
        if (self.__width == 0) or (self.__height == 0):
            return ""

        symbol = '#'
        rect_str = list()
        for row in range(self.__height):
            line = self.__width * symbol
            rect_str.append(line)

        rep = '\n'.join(rect_str)
        return (rep)

    def __repr__(self):
        """
        Return the canonical string representation of a Rectangle
        """
        rep = "{}({:d}, {:d})"
        rep = rep.format(type(self).__name__, self.__width, self.__height)
        return rep

    def __del__(self):
        """
        Print message when instance or Rectangle is deleted
        """
        print("Bye rectangle...")
