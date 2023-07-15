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

    def test_constructor(self):
        """
        Ensure the constructor behaves as expected
        """
        # Only positional arguments
        size = 5
        new = Square(size)

        x = 0
        y = 0
        attrs = {"size": size, "x": x, "y": y}
        for key, val in attrs.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(hasattr(new, key))
                self.assertEqual(getattr(new, key), val)
        del new

        # Positionals and keyword arguments
        size = 4
        _x = 4
        _y = 6
        _id = "I am square :)"
        new = Square(size, x=_x, y=_y, id=_id)

        attrs = {"size": size, "x": _x, "y": _y, "id": _id}
        for key, val in attrs.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(hasattr(new, key))
                self.assertEqual(getattr(new, key), val)
        del new

    def test_width_height(self):
        """
        Ensure that width and height of the Square is the same as size

        - A square is a rectangle with the same width and height values
        """
        size = 12
        new = Square(size)

        attrs = {"width": size, "height": size}
        for key, val in attrs.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(hasattr(new, key))
                self.assertEqual(getattr(new, key), val)
