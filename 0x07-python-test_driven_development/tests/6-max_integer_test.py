#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class to test the functionality of the ``max_integer`` function
    """

    def test_max_integer(self):
        """
        Contains alot of test cases for the function
        ``max_integer()``
        """

        self.assertEqual(max_integer([12, 4, 5]), 12)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([13]), 13)
