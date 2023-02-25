#!/usr/bin/python3
"""This module contains a class ``MyLlist`` that inherits from ``list``

Attributes:
    MyClass(list): a class that inherits from ``list``
"""


class MyList(list):
    """A class that inherits from list
    """

    def __init__(self):
        """Initialize the list
        """

        super().__init__()

    def print_sorted(self):
        """Prints the elements of the list in ascending order
        """

        new_list = list(self)
        new_list.sort()
        print(new_list)
        del(new_list)
