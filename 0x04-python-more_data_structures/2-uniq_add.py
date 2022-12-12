#!/usr/bin/python3

def uniq_add(my_list=[]):
    """A function that adds all unique integers in a list
       (only once for each integer).

        Args:
           my_list: a list of integers

        Return: sum of all unique integers
    """

    if not my_list:
        return my_list

    my_set = set(my_list)
    sum = int()
    for el in my_set:
        sum += int(el)
    return (sum)
