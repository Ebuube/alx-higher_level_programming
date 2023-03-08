#!/usr/bin/python3
"""
Create the ``Square`` class that inherits from the ``Rectangle`` class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Define the class ``Square``
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize an instance of the class ``Square``
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return the non-canonical string representation of the
        instance of ``Square``

        NB:
            To access private instance attributes declared in the super class:
            1) Ensure that the attribute has getter and setter defined in
                super class
            2) Access it via:

                self.<attr_name>
        """
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__,
                self.id,
                self.x,
                self.y,
                self.width)
