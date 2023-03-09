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

        Format:
        >> [<cls.__name__>] (<id>) <x>/<y> - <size>

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

    @property
    def size(self):
        """
        Retrieve the size of the ``Square`` instance
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Set the value of the size of the ``Square`` instance
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the instance of the class ``Square``

        NB: ORDER IS IMPORTANT

        1st argument = id
        2nd argument = size
        3rd argument = x
        4th argument = y

        kwargs is ignored if args exists and is not empty
        """

        for pos in range(len(args)):
            if pos == 0:
                self.id = args[pos]
            elif pos == 1:
                self.size = args[pos]
            elif pos == 2:
                self.x = args[pos]
            elif pos == 3:
                self.y = args[pos]

        # Skip this if *args already exist and is not empty, else execute it
        if len(args) == 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """
        Retrieve the dictionary representation of the ``Square`` instance
        """
        obj_dict = dict()
        obj_dict['id'] = self.id
        obj_dict['size'] = self.size
        obj_dict['x'] = self.x
        obj_dict['y'] = self.y

        return obj_dict
