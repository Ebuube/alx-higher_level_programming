#!/usr/bin/python3

def number_keys(a_dictionary):
    """A function that returns the number of keys in a dictionary
    Args:
        a_dictionary: a dictionary variable
    Returns:
        the number of keys in the dictionary
    """
    if not a_dictionary:
        return 0
    return (len(a_dictionary.keys()))
