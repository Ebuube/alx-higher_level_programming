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
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of ``list_objs`` to a file

        Args:
            list_objs: a list of instances which inherit from ``Base``
                        example: list of ``Rectangle`` or ``Square`` instances
        EXTRA:
            if ``list_objs`` is None, save an empty list
            The filename is ``<Class name>.json`` - example ``Rectangle.json``
            The file is overwritten each time the program is ran
        """

        filename = cls.__name__ + ".json"

        with open(filename, "w") as the_jsonfile:
            if list_objs is None:
                the_jsonfile.write("[]")
            else:
                # list_dicts = [x.to_dictionary() for x in list_objs]
                list_dicts = list()
                for x in list_objs:
                    list_dicts.append(x.to_dictionary())
                the_jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Retrive a list from a JSON string

        Args:
            json_string: a string representation of list of dictionaries
        Return:
            if ``json_string`` is None or empty, return an emtpy list
            else,
            Returns the list represented by ``json_string``
        """

        if (json_string is None) or (len(json_string) == 0):
            return list()
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Args:
            dictionary: key word arguments for initialization
        """
        if (not (dictionary is None)) and (len(dictionary)) != 0:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)

            new.update(**dictionary)
            return new
