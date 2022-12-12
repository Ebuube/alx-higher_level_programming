#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """A function that prints a dictionary by ordered keys.
    Args:
        a_dictionary: a dictionary variable
    Returns:
        nothing
    """
    if not a_dictionary:
        return None

    sorted_list_of_keys = sorted(dict(a_dictionary))
    for el in sorted_list_of_keys:
        print("{}: {}".format(el, a_dictionary.get(el)))
