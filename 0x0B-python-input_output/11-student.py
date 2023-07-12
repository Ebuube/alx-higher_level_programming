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

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of an instance
        If `attrs` is a list of strings, only attribute names in this list
        will be retrieved else, all attributes are retrieved
        """
        obj = dict()
        default = None

        if type(attrs) is list:
            for i in attrs:
                if type(i) is str and i in self.__dict__:
                    obj[i] = self.__dict__[i]
        else:
            return self.__dict__

        return obj

    def reload_from_json(self, json):
        """
        Replace all attributes of the instance with the JSON dict `json`
        Assumption:
            `json` is always a dictionary
            A key in the dictionary `json` is a public instance attribute
            A value in the dicionary `json` is the value of the attribute
        """
        for key, val in json.items():
            (self.__dict__)[key] = val
