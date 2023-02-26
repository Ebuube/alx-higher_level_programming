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
