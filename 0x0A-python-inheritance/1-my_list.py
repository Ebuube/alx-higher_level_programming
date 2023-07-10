#!/usr/bin/python3
"""
This module defines the 'MyList' class
"""


class MyList(list):
    """
    An extension of the list class
    """
    def print_sorted(self):
        """
        Print the list, but sorted (ascending sort)
        NB: the original list retains it's order
        """
        dup = self[:]
        dup.sort()
        print(dup)
