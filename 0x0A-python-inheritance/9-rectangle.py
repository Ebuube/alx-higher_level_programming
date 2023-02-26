#!/usr/bin/python3
"""This module contains the definition of the class ``BaseGeometry``
and another class ``Rectangle`` which inherits from ``BaseGeometry``
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Define the class
    """

    def __init__(self, width, height):
        """Initialize an instance of ``BaseGeometry``
        """

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculate the area of the ``Rectangle`` object
        """

        return (self.__width * self.__height)

    def __str__(self):
        """Return the string representation of the object
        """

        return ("[{}] {}/{}".format(type(self).__name__, self.__width,
                self.__height))
