#!/usr/bin/python3
"""
Create the ``Rectangle`` class that inherits from ``Base`` class
"""


from models.base import Base


class Rectangle(Base):
    """
    Define the class rectangle that inherits from the class ``Base``
    Private instance attributes:
    * __width -> width
    * __height -> height
    * __x -> x
    * __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize an instance of the class ``Rectangle``
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Retrieve the value of the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of the Rectangle's width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Retrieve the value of the Rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of the Rectangles's height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Retrieve the value of the private instance attribute ``x``
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the value of ``x``
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Retrieve the value of the private instance attribute ``y``
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the value of ``y``
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Return the area of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Print to stdout the ``Rectangle`` instance with the character
        ``#``
        Takes care of the x and y coordinates of the instance object
        """

        for y in range(self.__y):
            print()

        for height in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')

            for width in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """
        Return the non-canonical string representation of the
        ``Rectangle`` instance
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__,
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the instance object
        NOTE: THE ORDER IS VERY IMPORTANT

        1st argument = id
        2nd argument = width
        3rd argument = height
        4th argument = x
        5th argument = y

        kwargs is ignored if args exists and is not empty
        """

        for pos in range(len(args)):
            if pos == 0:
                self.id = args[pos]
            elif pos == 1:
                self.__width = args[pos]
            elif pos == 2:
                self.__height = args[pos]
            elif pos == 3:
                self.__x = args[pos]
            elif pos == 4:
                self.__y = args[pos]

        # Skip this if *args already exist and is not empty, else execute it
        if len(args) == 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """
        Retrieve the dictionary representation of the ``Rectangle`` instance
        """
        obj_dict = dict()
        obj_dict['id'] = self.id
        obj_dict['width'] = self.width
        obj_dict['height'] = self.height
        obj_dict['x'] = self.x
        obj_dict['y'] = self.y

        return obj_dict
