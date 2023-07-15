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
from models import config


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
