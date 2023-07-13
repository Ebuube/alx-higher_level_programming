#!/usr/bin/python3
"""
This module defines the class `Base`
"""


class Base:
    """
    Definition of the `Base` class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize an instance of the class
        """
        if not id is None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1
