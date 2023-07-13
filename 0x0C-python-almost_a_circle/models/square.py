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
        fmt = fmt.format(type(self).__name__, self.id, self.x, self.y,
                         self.width)
        return fmt
