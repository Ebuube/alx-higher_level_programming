#!/usr/bin/python3

def uniq_add(my_list=[]):
    """A function that adds all unique integers in a list
       (only once for each integer).

        Args:
           my_list: a list of integers

        Return: sum of all unique integers
            else zero (0) if error occurs
    """

    if my_list is None or len(my_list) == 0:
        return 0

    my_set = set(my_list)
    sum = int()
    for el in my_set:
        sum += int(el)
    return (sum)
