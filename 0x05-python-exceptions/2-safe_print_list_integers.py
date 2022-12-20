#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list and only
    integers

    Args:
        my_list: a list that contains any type
        x: number of elements of my_list to print
    Returns:
        The number of integers printed
    """
    count = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end='')
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return (count)
