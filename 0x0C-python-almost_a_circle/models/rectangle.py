#!/usr/bin/python3
"""
This module defines the `Rectangle` class
"""
from models.base import Base


class Rectangle(Base):
    """
    Definition of Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize and instance of the `Rectangle` class
        """
        super().__init__(id)

        # Use the `setter` to set the attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieve the `width` attribute
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieve the `height` attribute
        """
        return self.__height

    @property
    def x(self):
        """
        Retrieve the `x` attribute
        """
        return self.__x

    @property
    def y(self):
        """
        Retrieve the `y` attribute
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Set the `width` attribute
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the `height` attribute
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Set the `x` attribute
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Set the `y` attribute
        """
        self.__y = value
