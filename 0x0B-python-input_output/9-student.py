#!/usr/bin/python3
"""This module defines the class ``Student``
"""


class Student:
    """Define the class ``Student``
    """

    def __init__(self, first_name, last_name, age):
        """Initialize and instance of ``Student``
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance
        """

        return self.__dict__
