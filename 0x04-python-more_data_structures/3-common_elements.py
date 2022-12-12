#!/usr/bin/python3

def common_elements(set_1, set_2):
    """A function that returns a set of common elements in two sets

    Args:
        set_1: the first set of data
        set_2: the second set of data

    Returns: a set of the common elements in set_1 and set_2
    """
    if not set_1:
        return set_2
    if not set_2:
        return set_1

    set_3 = set(set_1) & set(set_2)
    return (set_3)
