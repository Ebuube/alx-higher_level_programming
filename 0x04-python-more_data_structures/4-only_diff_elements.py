#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """A function that returns a set of all elements in only one set
    Args:
        set_1: the first set
        set_2: the second set

    Returns:
        A set of elements in only one set
    """
    if not set_1 or len(set_1) == 0:
        return set_2
    if not set_2 or len(set_2) == 0:
        return set_1

    set_3 = set(set_1) ^ set(set_2)
    return (set_3)
