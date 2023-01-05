#!/usr/bin/python3
"""This module contains a function that says the name of a user

Attributes:
    say_my_name (def): function to say username
"""


def say_my_name(first_name, last_name=""):
    """Print user's name

    prints the string ``My name is <fist_name> <last_name>``

    Args:
        first_name (str): user's first name
        last_name (str): user's last name (optional)

    Usage:
        >>> say_my_name('Ebube', 'Onwuta')
        My name is Ebube Onwuta
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
