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
        self.heigth = height

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

        perimeter = 0
        if (self.__width == 0) or (self.__height == 0):
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)

        return perimeter

    def __str__(self):
        """Return the canonical string representation of the object
        """

        full_rect = []
        rect_row = '#' * self.__width

        if self.__height == 0 or self.__width == 0:
            return ""

        for row in range(self.__height):
            full_rect.append(rect_row)

        return '\n'.join(full_rect)

    def __repr__(self):
        """Return the canonical string representation of the object
        """
        w = self.__width
        h = self.__height
        return "Rectangle({:d}, {:d})".format(w, h)
