#!/usr/bin/python3
"""Module for Square class

This module contains the implementation of the class Square

Attributes:
    Square (class): Definition of the Square Class
"""


class Square:
    """Implementation of the class Square

    Attributes:
        __size (int): size of a side of the square represented
        __position (tuple): (x, y) position as integers
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square object

        Raises a TypeError if `size` is not int type
        Raises a ValueError if `size` is less than zero
        Position must be a tuple of 2 positive integers, otherwise it
        Raises a `TypeError` exception with the message
        `position must be a tuple of 2 positive integers`

        Args:
            size (int): size of a side of the square
            position (tuple): position of the square (x, y) axes
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) == tuple:
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) == 2:
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0]) == int) and (type(position[1]) == int):
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] >= 0) and (position[1] >= 0):
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculate the area of the square

        Returns:
            The area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieve the value of the object's size

        Returns:
            The value of of the object's size
        """
        return (self.__size)

    @size.setter
    def size(self, size=0):
        """Set the value of the object's size

        Args:
            size (int): size of a side of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must  be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Retrieve the value of the object's coordinates

        Returns:
            The coordinates of the object (x, y)
        """
        return (self.__position)

    @position.setter
    def position(self, position=(0, 0)):
        """Set the value of the object's coordinates

        Position must be a tuple of 2 positive integers, otherwise it
        Raises a `TypeError` exception with the message
        `position must be a tuple of 2 positive integers`

        Args:
            position (tuple): (x, y) coordinates of the object as integers
        """
        if type(position) == tuple:
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) == 2:
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0]) == int) and (type(position[1]) == int):
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] >= 0) and (position[1] >= 0):
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """Display square using `#` character

        If size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for y_pos in range(self.__position[1]):
                print()
            for y_axis in range(self.__size):
                for x_pos in range(self.__position[0]):
                    print('_', end='')
                for x_axis in range(self.__size):
                    print('#', end='')
                print()
