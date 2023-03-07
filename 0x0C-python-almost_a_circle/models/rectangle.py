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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Retrieve the value of the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Set the value of the Rectangle's width
        """
        if not isinstance(type(width), int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """
        Retrieve the value of the Rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Set the value of the Rectangles's height
        """
        if not isinstance(type(height), int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """
        Retrieve the value of the private instance attribute ``x``
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Set the value of ``x``
        """
        if not isinstance(type(x), int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """
        Retrieve the value of the private instance attribute ``y``
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Set the value of ``y``
        """
        if not isinstance(type(y), int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")

        self.__y = y
