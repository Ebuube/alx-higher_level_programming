#!/usr/bin/python3

def best_score(a_dictionary):
    """A function that returns a key with the biggest integer value
    Args:
        a_dictionary: dictionary variable
    Returns:
        a key with the biggest integer value
    """
    if not a_dictionary or len(a_dictionary) == 0:
        return None

    max_key = list(a_dictionary)
    max_key = max_key[0]
    for key in a_dictionary:
        if a_dictionary[max_key] < a_dictionary[key]:
            max_key = key
    return (max_key)
