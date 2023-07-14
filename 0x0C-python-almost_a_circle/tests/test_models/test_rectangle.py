#!/usr/bin/python3
"""
Test for the ``Rectangle`` class
"""
import io
from tests.test_models.test_base import test_Base
from models.rectangle import Rectangle
from unittest.mock import patch


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

    def test_display_0(self):
        """
        Validate ``display`` method with zero(0) values of ``x`` and ``y``
        """
        new = Rectangle(width=3, height=5, x=0, y=0)
        output = list()
        SYMBOL = '#'
        NEWLINE = '\n'
        STDOUT = 'sys.stdout'
        for x in range(new.height):
            row = new.width * SYMBOL
            output.append(row)
        output = NEWLINE.join(output) + NEWLINE

        with patch(STDOUT, new=io.StringIO()) as my_patch:
            new.display()
            foo = my_patch.getvalue()
            self.assertEqual(foo, output)

    def test_display_1(self):
        """
        Validate ``display`` method with zero(0) values of ``x`` and ``y``
        """
        new = Rectangle(width=3, height=5, x=3, y=11)
        output = list()
        SYMBOL = '#'
        SPACE = ' '
        NEWLINE = '\n'
        STDOUT = 'sys.stdout'

        # Move ``y`` steps down
        y_move = str(new.y * NEWLINE)
        # print("{}".format(self.y * '\n'), end='')

        # Add the x position
        for row in range(new.height):
            # print("{}".format((SPACE * self.x) + (SYMBOL * self.width)))
            x_move = (new.x * SPACE) + (new.width * SYMBOL)
            output.append(x_move)

        output = NEWLINE.join(output)
        output = y_move + output + NEWLINE

        with patch(STDOUT, new=io.StringIO()) as my_patch:
            new.display()
            foo = my_patch.getvalue()
            self.assertEqual(foo, output)

    def test_update_0(self):
        """
        Validate update with only ordered arguments
        ORDER: id, width, height, x, y
        """
        new = Rectangle(1, 1, 1, 1)
        width = 12
        height = 5
        x = 8
        y = 1
        _id = 9
        new.update(_id, width, height, x, y)

        attrs = {"width": width, "height": height, "id": _id, "x": x, "y": y}
        for key, val in attrs.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(hasattr(new, key))
                self.assertEqual(getattr(new, key), val)
