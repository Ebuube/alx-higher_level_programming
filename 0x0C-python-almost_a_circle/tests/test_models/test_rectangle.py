#!/usr/bin/python3
"""
Test for the ``Rectangle`` class
"""
from tests.test_models.test_base import test_Base
from models.rectangle import Rectangle


'''
class test_Rectangle(test_Base):
    """
    Define extra tests for the ``Rectangle`` class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the class' test
        """
        super().__init__(*args, **kwargs)
        self.value = Rectangle
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

    def test_attrs(self):
        """
        Ensure that attributes are complete
        """
        new = self.value(12, 3, 4, 6)
        attrs = ["id", "width", "height", "x", "y"]
        for attr in attrs:
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(new, attr))
'''
