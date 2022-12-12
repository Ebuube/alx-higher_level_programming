#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """A function tha deletes keys with a specific value in a dictionary
    Args:
        a_dictionary: dictionary object
        value: a PyObectj
    Returns:
        The same list but a modified version of it
    """
    if not a_dictionary:
        return None

    new_dict = dict(a_dictionary)
    for key in new_dict:
        if new_dict[key] == value:
            del a_dictionary[key]
    return (a_dictionary)
