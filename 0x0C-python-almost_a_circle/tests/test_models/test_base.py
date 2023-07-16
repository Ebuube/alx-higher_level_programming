#!/usr/bin/python3
"""
Test for ``Base`` class
"""
import unittest
import glob
import os
import pep8
import json
import re
from models.base import Base
from tests import config


class test_Base(unittest.TestCase):
    """
    Definition of test for the class
    """
    # Set maxDiff to see all output on error comparison
    maxDiff = None

    def __init__(self, *args, **kwargs):
        """
        Initialize the test instance
        """
        super().__init__(*args, **kwargs)
        self.value = Base
        self.name = self.value.__name__

    def setUp(self):
        """
        Set up the environment for each test method
        """
        # Remove previous json and csv files
        json_fmt = ".json"
        csv_fmt = ".csv"
        path = "./"     # path to work on

        for root, dirs, files in os.walk(path):
            for _file in files:
                if _file.endswith(json_fmt) or _file.endswith(csv_fmt):
                    file_path = os.path.join(root, _file)
                    os.remove(file_path)
                    if config.setUp_verbose is True:
                        print("Removed: '{}'".format(file_path))

    def tearDown(self):
        """
        Tear down method for each test
        """
        # Remove previous json and csv files
        json_fmt = ".json"
        csv_fmt = ".csv"
        path = "./"     # path to work on

        for root, dirs, files in os.walk(path):
            for _file in files:
                if _file.endswith(json_fmt) or _file.endswith(csv_fmt):
                    file_path = os.path.join(root, _file)
                    os.remove(file_path)
                    if config.tearDown_verbose is True:
                        print("Removed: '{}'".format(file_path))

    def test_Base_id(self):
        """
        Ensure that ``Base.id`` is implemented
        """
        # id is of right type
        foo = Base()
        self.assertTrue(type(foo.id) is int)

        # Each instance has a different id
        bar = Base()
        self.assertNotEqual(foo.id, bar.id)

        # Custom id is implemented
        var = 14
        baz = Base(var)
        self.assertEqual(baz.id, var)

    def test_check_pep8_conformance(self):
        """
        Ensure all *.py files are pep8 (or pycodestyle) compliant
        It is run only ``once`` during a test
        """
        if config.pep8_checked is False:
            path = "."
            style = pep8.StyleGuide(quite=False, show_source=True,
                                    verbose=config.pep8_verbose)
            result = style.check_files(paths=path)
            self.assertEqual(result.total_errors, 0, "Fix pep8")
            config.pep8_checked = True

    def test_dictionary_to_json_string(self):
        """
        Ensure that the method ``to_json_string`` performs as required

        * It should return a JSON string representation for a list of
            dictionaries.
        * If the list of dictionaries is None or empty, should return
            '[]' string
        """
        dsquare = {"id": 4, "size": 14, "x": 5, "y": 1}
        drectangle = {"id": 8, "width": 98, "height": 21, "x": 0, "y": 8}

        # list_dictionaries -> None
        # Should return '[]'
        list_dictionaries = None
        return_val = "[]"
        self.assertEqual(Base.to_json_string(list_dictionaries), return_val)

        # list_dictionaries -> [] i.e empty
        # Should return '[]'
        list_dictionaries = list()
        return_val = "[]"
        self.assertEqual(Base.to_json_string(list_dictionaries), return_val)

        # list_dictionaries -> not empty
        # Should return the json
        list_dictionaries = [dsquare, drectangle]
        self.assertEqual(Base.to_json_string(list_dictionaries),
                         json.dumps(list_dictionaries))

    def test_save_to_file_none(self):
        """
        Ensure that the method ``save_to_file()`` performs as required

        * If list of objects is None, saves an empty list i.e "[]"
        * The filename will be <Class name>.json - example: Base.json
        """
        _class = Base
        file_fmt = ".json"
        filename = _class.__name__ + file_fmt

        # list_objs -> None
        # Should save '[]'
        list_objs = None
        saved_val = "[]"
        self.assertFalse(os.path.exists(filename))
        _class.save_to_file(list_objs)
        self.assertTrue(os.path.exists(filename))

        # Analyze content of file
        mode = 'r'
        enc = "utf-8"   # UTF8 encoding
        with open(filename, mode, encoding=enc) as f:
            val = f.read()
            self.assertEqual(saved_val, val)

    def test_save_to_file_empty(self):
        """
        Ensure that the method ``save_to_file()`` performs as required

        * If list of objects is empty, saves an empty list i.e "[]"
        * The filename will be <Class name>.json - example: Base.json
        """
        _class = Base
        file_fmt = ".json"
        filename = _class.__name__ + file_fmt

        # list_objs -> empty -> list()
        # Should save '[]'
        list_objs = list()
        saved_val = "[]"
        self.assertFalse(os.path.exists(filename))
        _class.save_to_file(list_objs)
        self.assertTrue(os.path.exists(filename))

        # Analyze content of file
        mode = 'r'
        enc = "utf-8"   # UTF8 encoding
        with open(filename, mode, encoding=enc) as f:
            val = f.read()
            self.assertEqual(saved_val, val)

    def test_save_to_file_not_empty(self):
        """
        Ensure that the method ``save_to_file()`` performs as required

        * If list of objects is not empty and not None,
            saves a JSON representation of the objects
        * The filename will be <Class name>.json - example: Rectangle.json
        """
        from models.rectangle import Rectangle

        _class = Rectangle
        file_fmt = ".json"
        filename = _class.__name__ + file_fmt
        new1 = _class(id=41, width=4, height=8)
        new2 = _class(id=1, width=8, height=1)

        # list_objs -> not empty
        # Should save json string representation of objects
        list_objs = [new1, new2]
        list_dictionaries = list()

        # get dictionary representation of objects
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())

        # Save the objects to file
        saved_val = _class.to_json_string(list_dictionaries)
        self.assertFalse(os.path.exists(filename))
        _class.save_to_file(list_objs)
        self.assertTrue(os.path.exists(filename))

        # Analyze content of file
        mode = 'r'
        enc = "utf-8"   # UTF8 encoding
        with open(filename, mode, encoding=enc) as f:
            val = f.read()
            self.assertEqual(json.loads(saved_val), json.loads(val))

    def test_save_to_file_overwrite(self):
        """
        Ensure that the method ``save_to_file()`` overwrites existing file

        * If file exists, it should be overwritten by another call to
            ``save_to_file()`` method
        * The filename will be <Class name>.json e.g. Rectangle.json
        """
        from models.rectangle import Rectangle

        _class = Rectangle
        file_fmt = ".json"
        filename = _class.__name__ + file_fmt
        new1 = _class(id=41, width=4, height=8)
        new2 = _class(id=1, width=8, height=1)

        # list_objs -> not empty
        # Should save json string representation of objects
        list_objs = [new1, new2]

        # save objects to file
        self.assertFalse(os.path.exists(filename))
        _class.save_to_file(list_objs)
        self.assertTrue(os.path.exists(filename))

        # Fetch saved value
        previous_val = str()
        mode = 'r'
        enc = "utf-8"   # UTF8 encoding
        with open(filename, mode, encoding=enc) as f:
            previous_val = f.read()

        # Add new objects and resave
        new3 = _class(id=5, width=12, height=98)
        list_objs.append(new3)
        _class.save_to_file(list_objs)

        # Compare content of file with previous content
        mode = 'r'
        enc = "utf-8"   # UTF8 encoding
        with open(filename, mode, encoding=enc) as f:
            val = f.read()
            self.assertNotEqual(json.loads(previous_val), json.loads(val))

    def test_json_string_to_dictionary_none(self):
        """
        Ensure that an empty list is returned when a JSON string is None
        or empty.
        """
        from models.rectangle import Rectangle

        _class = Rectangle
        json_string = None
        empty_list = list()

        self.assertEqual(_class.from_json_string(json_string), empty_list)

    def test_json_string_to_dictionary_empty(self):
        """
        Ensure that an empty list is returned when a JSON string is
        an empty list string.
        """
        from models.rectangle import Rectangle

        _class = Rectangle
        json_string = json.dumps(list())
        empty_list = list()

        self.assertEqual(_class.from_json_string(json_string), empty_list)

    def test_json_string_to_dictionary(self):
        """
        Ensure a list of dictionaries is returned when the json_string is not
        empty or None
        """
        from models.rectangle import Rectangle

        _class = Rectangle
        d1 = {'height': 4, 'width': 10, 'id': 89}
        d2 = {'height': 7, 'width': 1, 'id': 7}
        list_dictionaries = [d1, d2]
        list_input = json.dumps(list_dictionaries)

        self.assertEqual(_class.from_json_string(list_input),
                         list_dictionaries)

    def test_dictionary_to_instance(self):
        """
        Ensure that an instance is returned by the ``create()``
        class method
        """
        from models.rectangle import Rectangle

        _class = Rectangle
        new1 = _class(1, 1, 1, 1)     # dummy instance
        d_attrs = {'width': 4, 'height': 7, 'x': 8, 'y': 12, 'id': 41}

        self.assertEqual(type(_class.create(**d_attrs)), _class)

        new2 = _class(**d_attrs)
        new1 = _class.create(**d_attrs)
        self.assertEqual(new2.to_dictionary(), new1.to_dictionary())

    def test_file_to_instances_file_absent(self):
        """
        Ensure that an empty list if file doesn't exist

        method = ``load_from_file``
        """
        from models.rectangle import Rectangle

        _class = Rectangle
        file_format = ".json"
        filename = _class.__name__ + file_format

        list_output = list()    # empty list

        # Ensure that file is absent
        self.assertFalse(os.path.exists(filename))

        self.assertEqual(_class.load_from_file(), list_output)

    def test_file_to_instances(self):
        """
        Ensure that a list of instances is returned by the method
        ``load_from_file`` class method
        """
        from models.rectangle import Rectangle

        _class = Rectangle
        file_format = ".json"
        filename = _class.__name__ + file_format
        new1 = _class(width=2, height=4, x=5, y=6, id=8)
        new2 = _class(width=5, height=1, x=8, y=13, id="My id")
        list_instances = [new1, new2]
        list_dictionaries = [new1.to_dictionary(), new2.to_dictionary()]

        self.assertFalse(os.path.exists(filename))
        _class.save_to_file(list_instances)
        self.assertTrue(os.path.exists(filename))

        list_input = _class.load_from_file()
        list_output = list()

        for instance in list_input:
            list_output.append(instance.to_dictionary())

        for instance_dict in list_output:
            with self.subTest(instance_dict=instance_dict):
                self.assertTrue(instance_dict in list_dictionaries)
