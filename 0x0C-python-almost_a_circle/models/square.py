#!/usr/bin/python3
"""
This module defines the ``Square`` class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Definition of the class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize an instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return non-canonical string representation of an instance
        Format: ``[Square] (<id>) <x>/<y> - <size>``
        """
        fmt = "[{}] ({}) {}/{} - {}"
        fmt = fmt.format(self.__class__.__name__, self.id, self.x, self.y,
                         self.width)
        return fmt

    @property
    def size(self):
        """
        Retrieve the ``size`` of an instance
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the ``size`` of an instance
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        * Update the instance with no-keyword arguments in this order
            1) id
            2) size
            3) x    # position
            4) y    # position
            Argument order is super important

        * Update the instance using keyword-arguments (dictionary)
            - Each key in this dictionary represents an attribute to the
                instance.
            - Order is not important

        NB: ``**kwargs`` are skipped if ``*args`` exists and is not empty.
        """
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass    # argument not supplied -> leave it un-updated

        # Skip ``kwargs`` if args exists and is not empty
        if not (args and (len(args) > 0)):
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
        Retrieve the dictionary representation of a Square
        It contains: "id", "size", "x", "y" and ...
        """
        obj_dict = super().to_dictionary()

        # Remove unrelated key/value pairs and add new key/value pair
        rect_attrs = ["height", "width"]    # attributes of a Rectangle
        for attr in rect_attrs:
            obj_dict.pop(attr, None)

        key = "size"
        obj_dict[key] = self.size

        return obj_dict
