#!/usr/bin/python3

def weight_average(my_list=[]):
    """A function that returns the weighted average of all integers tuple
    (<score>, <weight>)
    Example:
    my_list = [(1, 2), (9, 3), (8, 2), (4, 2)]
    # = ((1 * 2) + (9 * 3) + (8 * 2) + (4 * 2)) / (2 + 3 + 2 + 2)

    Args:
        my_list: a list object
    Returns:
        The weighted average of the list
    """
    if type(my_list) is not list or len(my_list) == 0:
        return 0.00

    sum_values = sum(list(map((lambda x: x[0] * x[1]), my_list)))
    sum_weight = sum(list(map((lambda x: x[1]), my_list)))
    wt_average = sum_values / sum_weight
    return (wt_average)
