#!/usr/bin/python3
"""
THIS MODULE CREATES BASE CLASS
"""


import json
import csv


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

        with open(filename, 'w') as the_jsonfile:
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
            elif cls.__name__ == "Square":
                new = cls(1)

            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Return the list of instances from <classname>.json file

        If the file doesn't exit, return an empty list

        Otherwise, return a list of instances

        The type of these instances depend on ``cls``
        i.e. (current class using this method)

        NOTE:
            This function reads from ``<cls.__name__>.json``
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as json_file:

                # list_dicts: list of dictionaries represented by json string
                list_dicts = Base.from_json_string(json_file.read())

                # instance: a list of instances whether Rectangle or Squares
                instance = list()

                # obj: is a dictionary variable
                for obj in list_dicts:
                    instance.append(cls.create(**obj))

                return instance
        except IOError:
            return list()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialze all the instances in ``list_objs`` to a the file
        ``<Class name>.csv``, eg ``Rectangle.csv``

        Args:
            list_objs: a list of instances of ``cls``

        Format:
            For Rectangle: <id>, <width>, <height>, <x>, <y>
            For Square: <id>, <size>, <x>, <y>

        NOTE:

            *   The csv file created has a header in the format above

            *   This method overwrites any pre-existing file bearing the name
                ``<Class name>.csv``. Otherwise, a new one is created
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as csvfile:

            # Set fieldnames
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']

            # Setting DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_NONNUMERIC)

            # Write the header of the file
            writer.writeheader()

            if list_objs and (len(list_objs) > 0):

                # list_dicts: a list of dictionaries gotten from list_objs
                list_dicts = list()

                # Convert each object to a dictionary and add them to list
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())

                # Write each dict representation of list_objs to csvfile
                for obj in list_dicts:
                    writer.writerow(obj)
            else:
                # Write an empty dictionary to csvfile
                writer.writerow(dict())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialze all the dictionary entries in the file ``<Class name>.csv``
        to a list of instances of the class ``<Class name>``

        Format:
            For Rectangle: <id>, <width>, <height>, <x>, <y>
            For Square: <id>, <size>, <x>, <y>

        Return:
            *   If file exists return a list of instances

            *   If the specified file doesn't exist, return an emtpy list

        NOTE:

            *   The csv file to be opened has a header in the format above
        """
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, 'r', newline='') as csvfile:

                # Set fieldnames
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fieldnames = ['id', 'size', 'x', 'y']

                # Setting DictReader object
                # NB: the fieldnames argument is optional
                reader = csv.DictReader(csvfile, fieldnames=fieldnames,
                                        quoting=csv.QUOTE_NONNUMERIC)

                # list_objs: a list of instances to be returned
                list_objs = list()

                # read_header: used to know if the header has been read
                read_header = False

                # Read each row of the csvfile as a dictionary
                # Create an instance out of this dictionary
                # And add it to the ``list_objs`` list
                for row in reader:

                    # Skip the header
                    if read_header is False:
                        read_header = True
                        continue

                    # convert each numeric field to int
                    for key in row:
                        if type(row[key]) == float:
                            row[key] = int(row[key])

                    list_objs.append(cls.create(**row))

                # returning the list of instances
                return list_objs

        except IOError:
            # Return an empty list if file doesn't exist
            return list()
