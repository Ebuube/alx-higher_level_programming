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


class test_base(unittest.TestCase):
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

        # obtain source code
        delim = '.'
        self._sep = '/'
        fmt = ".py"
        # pattern : <class 'models.base.Base'>
        pattern = ".*\'(.*\.*.*\.*.*)\'.*"
        result = re.search(pattern, str(self.value))
        track = result.group(1)
        track = (track.split(delim))[:-1]
        track = self._sep.join(track)
        track = track + fmt
        if os.path.exists(track):
            self._source_code = track

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

    def test_package(self):
        """
        Ensure that ``__init__.py`` file is present in `models` directory
        """
        package = "__init__.py"
        path = ((self._source_code.split(self._sep)[0]) + self._sep +
                "{}".format(package))
        self.assertTrue(os.path.exists(path))

    def test_pep8(self):
        """
        Ensure that source code is Pep8 or pycodestyle compliant
        """
        style = pep8.StyleGuide(quite=False)
        p = style.check_files([self._source_code])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """
        Ensure that the module and its contents have docstrings
        """
        # module = (self._source_code.split(self._sep))[-1]
        # to be completed
        pass

    def test_executable_file(self):
        """
        Ensure that the source code has executable access for the users
        """

        """Check for read access"""
        is_read_true = os.access(self._source_code, os.R_OK)
        self.assertTrue(is_read_true)

        """Check for write access"""
        is_write_true = os.access(self._source_code, os.W_OK)
        self.assertTrue(is_write_true)

        """Check for execution access"""
        is_exec_true = os.access(self._source_code, os.X_OK)
        self.assertTrue(is_exec_true)
