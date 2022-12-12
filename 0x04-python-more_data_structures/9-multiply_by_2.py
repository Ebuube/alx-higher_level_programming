#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary
       with all values multiplied by 2
    Args:
        a_dictionary: dictionary variable
    Returns:
        a dictionary with the same key but the values are twice the
        corresponding variable in a_dictionary
    """
    if not a_dictionary or len(a_dictionary) == 0:
        return None

    new_dict = {}
    for key in a_dictionary:
        new_dict.setdefault(key, a_dictionary[key] * 2)
    return (new_dict)
