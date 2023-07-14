#!/usr/bin/python3
"""
Test for the ``Rectangle`` class
"""
from tests.test_models.test_base import test_Base
from models.rectangle import Rectangle


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

    def test_rectangle_attrs(self):
        """
        Ensure that attributes are complete
        """
        new = Rectangle(12, 3, 4, 6)
        attrs = ["id", "width", "height", "x", "y"]
        for attr in attrs:
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(new, attr))

    def test_rectangle_constructor(self):
        """
        Ensure that the constructuor can set attributes
        """
        width = 5
        height = 7
        x = 1
        y = 5
        _id = 14
        new = Rectangle(width, height, x, y, _id)

        attrs = {'id': _id, 'width': width, 'height': height, 'x': x, 'y': y}
        for attr in attrs:
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(new, attr))
                self.assertTrue(getattr(new, attr) == attrs[attr])

    def test_constr_default_args(self):
        """
        Ensure that the right default arguments are used
        """
        new = Rectangle(10, 2)
        defaults = {'x': 0, 'y': 0}

        for key, val in defaults.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(getattr(new, key) == val)

    def test_validate_attr_type(self):
        """
        Ensure that the ``type`` are validated before assignment
        """
        with self.assertRaises(TypeError):
            new = Rectangle(width='12', height=3, x=4, y=5, id=14)
        with self.assertRaises(TypeError):
            new = Rectangle(width=12, height='3', x=4, y=5, id=14)
        with self.assertRaises(TypeError):
            new = Rectangle(width=12, height=3, x='4', y=5, id=14)
        with self.assertRaises(TypeError):
            new = Rectangle(width=12, height=3, x=4, y='5', id=14)

    def test_validate_attr_value(self):
        """
        Ensure that the ``value`` of attributes are validated before assignment
        """
        # Validate width and height
        with self.assertRaises(ValueError):
            new = Rectangle(width=0, height=3, x=4, y=5)
        with self.assertRaises(ValueError):
            new = Rectangle(width=4, height=0, x=12, y=8)
        with self.assertRaises(ValueError):
            new = Rectangle(width=-3, height=3, x=4, y=5)
        with self.assertRaises(ValueError):
            new = Rectangle(width=2, height=-3, x=12, y=8)

        # Validate x and y positions
        with self.assertRaises(ValueError):
            new = Rectangle(width=1, height=1, x=-3, y=5)
        with self.assertRaises(ValueError):
            new = Rectangle(width=1, height=1, x=3, y=-3)

    def test_area(self):
        """
        Ensure area is properly calculated
        """
        new = Rectangle(width=5, height=3)
        self.assertEqual(new.area(), new.width * new.height)

    def test_string(self):
        """
        Validate that the `Rectangle`'s ``__str__``
        """
        new = Rectangle(width=3, height=4)
        string = "[{}] ({}) {}/{} - {}/{}"
        string = string.format(type(new).__name__, new.id, new.x, new.y,
                               new.width, new.height)
        self.assertEqual(string, str(new))
