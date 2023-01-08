#!/usr/bin/python3
"""This module contains a class ``Rectangle``
"""


class Rectangle:
    """Defines the class ``Rectangle``
    """

    def __init__(self, width=0, height=0):
        """Initialize an instance of the class  ``Rectangle``
        """

        self.__width = 0
        self.__height = 0

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle object
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Set the height of the Rectangle object
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle object
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle object
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle object
        """

        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle object
        """

        return 2 * (self.__width + self.__height)
