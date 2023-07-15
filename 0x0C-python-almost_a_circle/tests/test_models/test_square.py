#!/usr/bin/python3
"""
Tests for the ``Square`` class
"""
from tests.test_models.test_rectangle import test_Rectangle
from models.square import Square


class test_Square(test_Rectangle):
    """
    Define extra tests for the ``Square`` class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the class' test
        """
        super().__init__(*args, **kwargs)
        self.value = Square
        self.name = self.value.__name__

    def setUp(self):
        """
        Set up for tests
        """
        super().setUp()

    def tearDown(self):
        """
        Tear down for the tests
        """
        super().tearDown()
