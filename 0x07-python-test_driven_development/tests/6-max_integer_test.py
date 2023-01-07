#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class to test the functionality of the ``max_integer`` function
    """

    def test_unordered_list(self):
        """
        Contains alot of test cases for the function
        ``max_integer()``
        """

        self.assertEqual(max_integer([12, 4, 5]), 12)

    def test_ordered_list(self):
        """Tests an ordered list
        """

        self.assertEqual(max_integer([1, 5, 39]), 39)

    def test_same_values_in_lisst(self):
        """Tests a list with the same value in all the elements
        """

        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_floats(self):
        """Tests when the list contains floats
        """

        self.assertEqual(max_integer([3.4, -83, 0.00]), 3.4)

    def test_strings_in_list(self):
        """Test when the list contains strings
        """

        self.assertEqual(max_integer("abcde"), 'e')

    def test_empty_list(self):
        """Test when the list is empty
        """

        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test a list with only one element
        """

        self.assertEqual(max_integer([5]), 5)

    def test_no_argument_supplied(self):
        """Test when no argument is supplied to the function
        """

        self.assertIsNone(max_integer())
