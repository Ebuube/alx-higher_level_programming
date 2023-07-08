#!/usr/bin/python3

def common_elements(set_1, set_2):
    """A function that returns a set of common elements in two sets

    Args:
        set_1: the first set of data
        set_2: the second set of data

    Returns: a set of the common elements in set_1 and set_2
            else return an empty list
    """
    if not set_1 or len(set_1) == 0:
        return []
    if not set_2 or len(set_2) == 0:
        return []

    set_3 = set(set_1) & set(set_2)
    return (set_3)
