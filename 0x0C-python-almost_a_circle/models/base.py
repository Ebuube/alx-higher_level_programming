#!/usr/bin/python3
"""
THIS MODULE CREATES BASE CLASS
"""


class Base():
    """
    Define the Base Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize an instance of the Base class
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
