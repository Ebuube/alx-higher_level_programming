#!/usr/bin/python3
"""
THIS MODULE CREATES BASE CLASS
"""


import json


class Base():
    """
    Define the Base Class

    This forms the basis for other subsequent classes
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of the argument

        Args:
            list_dictionaries = a list of dictionaries
        Return:
            if ``list_dictionaries`` is None or empty,
            return string ``""[]""``
        """
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.JSONEncoder().encode(list_dictionaries)
