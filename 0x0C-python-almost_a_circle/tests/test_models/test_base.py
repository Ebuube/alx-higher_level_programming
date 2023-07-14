#!/usr/bin/python3
"""
Test for ``Base`` class
"""
import unittest
import glob
import os
import pep8
import re
from models.base import Base


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
        json_files = glob.glob("*.json")
        csv_files = glob.glob("*.csv")
        files = json_files + csv_files

        for file_path in files:
            os.remove(file_path)

    def tearDown(self):
        """
        Tear down method for each test
        """
        # Remove previous json and csv files
        json_files = glob.glob("*.json")
        csv_files = glob.glob("*.csv")
        files = json_files + csv_files

        for file_path in files:
            os.remove(file_path)

    def test_id(self):
        """
        Ensure that ``Base.id`` is implemented
        """
        # id is of right type
        foo = self.value()
        self.assertTrue(type(foo.id) is int)

        # Each instance has a different id
        bar = self.value()
        self.assertNotEqual(foo.id, bar.id)

        # Custom id is implemented
        var = 14
        baz = self.value(var)
        self.assertEqual(baz.id, var)
