#!/usr/bin/python3
"""This module contains a class ``Rectangle``
"""


class Rectangle:
    """Defines the class ``Rectangle``
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize an instance of the class  ``Rectangle``
        """

        self.__width = 0
        self.__height = 0

        self.width = width
        self.heigth = height

        type(self).number_of_instances += 1

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

    def __str__(self):
        """Return the informal string representation of the object
        """

        full_rect = []
        rect_row = str(self.print_symbol) * self.__width

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

    def __del__(self):
        """Display message when an instance is deleted
        """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size
        """

        new = Rectangle(size, size)

        return new