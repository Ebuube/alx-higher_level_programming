#!/usr/bin/python3
"""
This module defines the class `Base`
"""
import json
import os
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation of ``json_string``

        * ``json_string`` is a string representing a list of dictionaries
        * If ``json_string`` is None or empty, Returns an empty list
        * Else Return the list represented by ``json_string``
        """
        if json_string is None or len(json_string) == 0:
            return list()

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of a list of objects to a file

        * filename -> <Class name>.json
        * ``list_objs`` -> a list of instances that inherit from ``Base``

        If ``list_objs`` is None, saves an empty list.

        NB: file is overwritten if it already exists.
        """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = list()

        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        objs_json = cls.to_json_string(list_dictionaries)

        mode = 'w'  # write mode
        enc = "utf-8"   # UTF8 encoding
        with open(filename, mode, encoding=enc) as f:
            f.write(objs_json)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the object to a CSV file name
        * fileanme -> <Class name>.csv
        * Format of the CSV

        For Rectangle:
        <id>,<width>,<height>,<x>,<y>

        For Square:
        <id>,<size>,<height>,<x>,<y>
        """
        filename = "{}.csv".format(cls.__name__)
        list_dictionaries = list()

        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        mode = 'w'  # write mode
        enc = "utf-8"   # UTF8 encoding
        delim = ','     # delimiter
        # Create fields
        fields = list()
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]

        with open(filename, mode, encoding=enc) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields,
                                    delimiter=delim, quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)

            writer.writeheader()     # write the fields
            for row in list_dictionaries:
                writer.writerow(row)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance of the class ``cls`` with all attributes already set

        * ``dictionary`` is a dictionary of attributes
        """
        new = cls(1, 1, 0)      # dummy attributes
        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances saved to the file ``<Class name>.json``

        * If file doesn't exist, returns an empty list.
        """
        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return list()

        # Read JSON file
        objs_json = str()
        mode = 'r'
        enc = "utf-8"   # UTF8 encoding
        with open(filename, mode, encoding=enc) as f:
            objs_json = f.read()

        # Create a list of dictionaries representing objects
        objs_dict_list = Base.from_json_string(objs_json)
        objs = list()
        for obj_dict in objs_dict_list:
            objs.append(cls.create(**obj_dict))

        return objs

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of instances saved to the file ``<Class name>.csv``

        * If file doesn't exist, returns an empty list.
        """
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return list()

        # Read CSV file
        objs = list()   # list of instances to be returned
        mode = 'r'      # read mode
        enc = "utf-8"   # UTF8 encoding
        delim = ','     # delimiter used
        # Create fields
        fields = list()
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]

        with open(filename, mode, encoding=enc) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fields,
                                    delimiter=delim, quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)

            header = next(reader)   # ignore the header
            header_fields = [key for key in header.keys()]
            if header_fields != fields:
                print("Warning: header_fields is different from object fields",
                      file=sys.stderr)
                print("header_fields: {}".format(header_fields),
                      file=sys.stderr)
                print("object fields: {}".format(fields), file=sys.stderr)

            for obj_dict in reader:
                # Convert integers
                for key, val in obj_dict.items():
                    try:
                        obj_dict[key] = int(val)
                    except (ValueError, TypeError):
                        pass    # leave the value as it is
                # Create instance
                objs.append(cls.create(**obj_dict))

        return objs
