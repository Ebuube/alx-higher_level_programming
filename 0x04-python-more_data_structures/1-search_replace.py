#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """A function that replaces all occurences of an element by another
       in a new list

    Args:
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element

    Returns:
        The a list that contains the replaced elements
    """
    res = []

    if not my_list:
        return my_list

    for element in my_list:
        if element == search:
            res.append(replace)
        else:
            res.append(element)
    return (res)
