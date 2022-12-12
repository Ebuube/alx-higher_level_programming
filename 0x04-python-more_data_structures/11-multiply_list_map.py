#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """A function that returns a list with all values multiplied by a number
    without using any loops.
    Args:
        my_list = a list variable
        number = a numerical variable
    Returns:
        a list with the values multiplied by a number
    """
    if not my_list:
        return None

    new_list = list(map((lambda element: element * number), my_list))
    return (new_list)
