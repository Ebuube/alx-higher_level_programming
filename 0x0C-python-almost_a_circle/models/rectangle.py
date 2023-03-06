#!/usr/bin/python3
"""
Create the ``Rectangle`` that inherits from ``Base``
"""


from models.base import Base


class Rectangle(Base):
    """
    Define the class rectangle that inherits from the class ``Base``
    Private instance attributes:
    * __width -> width
    * __height -> height
    * __x -> x
    * __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize an instance of the class ``Rectangle``
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Retrieve the value of the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, a_width):
        """
        Set the value of the Rectangle's width
        """
        if not isinstance(a_width, int):
            raise TypeError("width must be an integer")
        if a_width <= 0:
            raise ValueError("width must be > 0")

        self.__width = a_width

    @property
    def height(self):
        """
        Retrieve the value of the Rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, a_height):
        """
        Set the value of the Rectangles's height
        """
        if not isinstance(a_height, int):
            raise TypeError("height must be an integer")
        if a_height <= 0:
            raise ValueError("height must be > 0")

        self.__height = a_height

    @property
    def x(self):
        """
        Retrieve the value of the private instance attribute ``x``
        """
        return self.__x

    @x.setter
    def x(self, a_x):
        """
        Set the value of ``x``
        """
        if not isinstance(a_x, int):
            raise TypeError("x must be an integer")
        if a_x < 0:
            raise ValueError("x must be >= 0")

        self.__x = a_x

    @property
    def y(self):
        """
        Retrieve the value of the private instance attribute ``y``
        """
        return self.__y

    @y.setter
    def y(self, a_y):
        """
        Set the value of ``y``
        """
        if not isinstance(a_y, int):
            raise TypeError("y must be an integer")
        if a_y < 0:
            raise ValueError("x must be >= 0")

        self.__y = a_y
