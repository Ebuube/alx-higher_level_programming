#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """A function that deletes a key in a dictionary
    Args:
        a_dictionary: dictionary variable
        key: key to delete along with its value
    Returns:
        The modified version of a_dictionary
    """

    if not a_dictionary:
        return None

    try:
        del a_dictionary[key]
    except KeyError:    # if key is non-existent, do nothing
        a_dictionary
    return (a_dictionary)
