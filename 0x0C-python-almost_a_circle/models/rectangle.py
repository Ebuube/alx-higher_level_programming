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
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Retrieve the value of the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of the Rectangle's width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieve the value of the Rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of the Rectangles's height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Retrieve the value of the private instance attribute ``x``
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the value of ``x``
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Retrieve the value of the private instance attribute ``y``
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the value of ``y``
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Return the area of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Print to stdout the ``Rectangle`` instance with the character
        ``#``
        """

        for height in range(self.__height):
            for width in range(self.__width):
                print('#', end='')
            print()
