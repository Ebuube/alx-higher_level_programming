#!/usr/bin/python3
"""
This module defines the ``Rectangle`` class
"""
from models.base import Base


class Rectangle(Base):
    """
    Definition of Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize and instance of the ``Rectangle`` class
        """
        super().__init__(id)

        # Use the ``setter`` to set the attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieve the ``width`` attribute
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieve the ``height`` attribute
        """
        return self.__height

    @property
    def x(self):
        """
        Retrieve the ``x`` attribute
        """
        return self.__x

    @property
    def y(self):
        """
        Retrieve the ``y`` attribute
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Set the ``width`` attribute
        * ``value`` must be an integer greater than zero(0)
        """
        name = "width"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the ``height`` attribute
        * ``value`` must be an integer greater than zero(0)
        """
        name = "height"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Set the ``x`` attribute
        * ``value`` must be an integer greater than or equal to zero(0)
        """
        name = "x"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Set the ``y`` attribute
        * ``value`` must be an integer greater than or equal to zero(0)
        """
        name = "y"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
        self.__y = value

    def area(self):
        """
        Retrieve the ``area`` value
        """
        return self.width * self.height

    def display(self):
        """
        Print an instance with the '#' character to stdout
        """
        SYMBOL = '#'
        SPACE = ' '

        # Move ``y`` steps down
        print("{}".format(self.y * '\n'), end='')

        # Add the x position
        for row in range(self.height):
            print("{}".format((SPACE * self.x) + (SYMBOL * self.width)))

    def __str__(self):
        """
        Return a non-canonical string representation of the instance
        """
        fmt = "[{}] ({}) {}/{} - {}/{}"
        fmt = fmt.format(self.__class__.__name__, self.id, self.x, self.y,
                         self.width, self.height)
        return fmt

    def update(self, *args, **kwargs):
        """
        * Update the instance with no-keyword arguments in this order
            1) id
            2) width
            3) height
            4) x    # position
            5) y    # position
            Argument order is super important

        * Update the instance using keyword-arguments (dictionary)
            - Each key in this dictionary represents an attribute to the
                instance.
            - Order is not important

        NB: ``**kwargs`` are skipped if ``*args`` exists and is not empty.
        """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass    # argument not supplied -> leave it un-updated

        # Skip ``kwargs`` if args exists and is not empty
        if not (args and (len(args) > 0)):
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
        Retrieve the dictionary representation of a `Rectangle`
        It contains: "id", "width", "height", "x", "y" and ...
        """
        # Obtain name mangling string
        self.__pevcae425jcea_mangling = None
        search_str = "pevcae425jcea_mangling"
        replacement = ''    # to securely remove the mangling
        key_plus_mangling = str()
        for key in self.__dict__.keys():
            if search_str in key:
                key_plus_mangling = key
                break

        del self.__pevcae425jcea_mangling   # remove test case
        mangling = key_plus_mangling.replace(search_str, replacement)
        # print("mangling = {}".format(mangling))

        # Retrieve values and remove the name mangling from keys
        obj_dict = dict()
        for key, val in self.__dict__.items():
            if mangling in key:
                key = key.replace(mangling, replacement)

            obj_dict.update({key: val})

        # Assertion
        attrs = ["id", "width", "height", "x", "y"]
        for item in attrs:
            if item not in obj_dict:
                msg = """'{}' not in dictionary representation.
                Rquirement Failure.
                """.format(item)
                raise Exception(msg)

        return obj_dict
