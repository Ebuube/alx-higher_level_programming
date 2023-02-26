#!/usr/bin/python3
"""This module contains the definition of the class ``MyInt`` which
inherits from the class ``int``
"""


class MyInt(int):
    """Define the class
    """

    def __eq__(self, other_int):
        """Define the equal (==) magic method
        Note: this class's normal function has been inverted
        """

        return super().__ne__(other_int)

    def __ne__(self, other_int):
        """Define the not equal (!=) magic method
        Note: this class's normal function has been inverted
        """

        return super().__eq__(other_int)
