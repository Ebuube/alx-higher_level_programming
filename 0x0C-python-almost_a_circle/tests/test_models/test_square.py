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

    def test_string(self):
        """
        Validate that the `Square`'s ``__str__``
        Format: [Square] (<id>) <x>/<y> - <size>
        """
        size = 10
        _x = 5
        _y = 9
        new = Square(size, x=_x, y=_y)
        string = "[{}] ({}) {}/{} - {}"
        string = string.format(type(new).__name__, new.id, new.x, new.y,
                               new.size)
        self.assertEqual(string, str(new))

    def test_setter_getter_attrs(self):
        """
        Ensure ``Square`` has setter and getter methods for ``size`` attribute

        To check for getter -> fget
        >>> Square.size.fget is not None

        To check for setter -> fset
        >>> Square.size.fset is not None
        """
        methods = {"fset": "fset", "fget": "fget"}
        attrs = {"size": "size", "x": "x", "y": "y", "width": "width",
                 "height": "height"}

        for attr in attrs.keys():
            for method in methods.keys():
                with self.subTest(method=method, attr=attr):
                    self.assertTrue(hasattr(Square, attr))
                    my_property = getattr(Square, attr)
                    self.assertTrue(getattr(my_property, method) is not None)

    def test_update_0(self):
        """
        Validate update with only ordered arguments
        ORDER: id, size, x, y
        """
        new = Square(1, 1, 1)
        size = 5
        x = 8
        y = 1
        _id = 9
        args = (_id, size, x, y)
        new.update(*args)

        attrs = {"size": size, "id": _id, "x": x, "y": y}
        for key, val in attrs.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(hasattr(new, key))
                self.assertEqual(getattr(new, key), val)

    def test_update_1(self):
        """
        Validate update with key-worded arguments
        ``**kwargs`` must be skipped if ``*args`` exists and is not empty
        """
        # Using only key-worded arguments
        new = Square(1, 1, 1)
        kwargs = {"size": 14, "x": 90, "y": 12, "id": "rect bar"}

        new.update(**kwargs)
        for key, val in kwargs.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(hasattr(new, key))
                self.assertEqual(getattr(new, key), val)
        del new

        # Using both *args and **kwargs
        # The *args should be implemented, leaving the **kwargs
        new = Square(1, 1, 1)
        _id = "rect foo"
        size = 13
        x = 9
        y = 3
        args = (_id, size, x, y)

        new.update(*args, **kwargs)
        for key, val in kwargs.items():
            with self.subTest(key=key, val=val):
                self.assertNotEqual(getattr(new, key), val)
        del new

        # Using an empty *args and a non-empty **kwargs
        # The **kwargs should be implemented, leaving the *args
        new = Square(1, 1, 1)
        args = ()

        new.update(*args, **kwargs)
        for key, val in kwargs.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(hasattr(new, key))
                self.assertEqual(getattr(new, key), val)
        del new

        # Not using *args, but a non-empty **kwargs
        # The **kwargs should be implemented, leaving the *args
        new = Square(1, 1, 1)

        new.update(**kwargs)
        for key, val in kwargs.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(hasattr(new, key))
                self.assertEqual(getattr(new, key), val)
        del new

        # Not using both *args and **kwargs
        new = Square(1, 1, 1)
        new.update()

        for key, val in kwargs.items():
            with self.subTest(key=key, val=val):
                self.assertTrue(hasattr(new, key))
                self.assertNotEqual(getattr(new, key), val)
        del new

    def test_to_dictionary(self):
        """
        Ensure that ``to_dictionary()`` method returns good a representation

        The returned dictionary must contain:
        id, size, x and y attributes with same values as the instance
        that returned them.
        """
        _class = Square
        _method = "to_dictionary"
        _id = "new Square"
        _size = 12
        _x = 8
        _y = 0
        new = _class(id=_id, size=_size, x=_x, y=_y)

        attrs = {"id": _id, "size": _size, "x": _x, "y": _y}

        # Ensure class has the method ``_method``
        self.assertTrue(hasattr(_class, _method))
        self.assertTrue(getattr(_class, _method) is not None)

        for key, val in new.to_dictionary().items():
            with self.subTest(key=key, val=val):
                self.assertEqual(attrs[key], val)
