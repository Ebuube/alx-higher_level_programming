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

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance
        If ``attrs`` is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes are retrieved
        """

        new_dict = dict()

        if attrs is None:
            return self.__dict__

        for attr in attrs:
            try:
                new_dict[attr] = self.__dict__[attr]
            except KeyError:
                continue

        return new_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance
        Using the supplied json representation

        Where, json is a dictionary
        """

        for attr in json:
            try:
                self.__dict__[attr] = json[attr]
            except KeyError:
                continue
