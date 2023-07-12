#!/usr/bin/python3
"""
This module implements the class `Student`
"""


class Student:
    """
    Definition of the class
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize an instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of an instance
        """
        return self.__dict__
