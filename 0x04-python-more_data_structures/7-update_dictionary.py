#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """A function that replaces or adds key/value in a dictionary
    Args:
        a_dictionary: a dictionary variable
        key: the key to add/replace its value
        value: the value to insert
    Returns:
        modified dictionary
    """
    if not a_dictionary:
        return None

    try:
        a_dictionary[key] = value
    except KeyError:    # if key is non-existent
        a_dictionary.setdefault(key, value)

    return (a_dictionary)
# end of function
