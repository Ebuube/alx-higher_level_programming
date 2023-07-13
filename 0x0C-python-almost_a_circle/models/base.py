#!/usr/bin/python3
"""
This module defines the class `Base`
"""
import json


class Base:
    """
    Definition of the `Base` class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize an instance of the class
        """
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries

        If ``list_dictionaries`` is None or empty, returns the string "[]"
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
