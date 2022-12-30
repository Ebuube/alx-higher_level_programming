#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """A function that divides element by element 2 list
    both lists can contain any type (integer, string, etc.)
    list_length can be bigger than the length of both lists

    Args:
        my_list_1: the first list object
        my_list_2: the second list object

    Returns:
        a list contain the value of a division between my_list_1[x] and
        my_list_2[x]
    """

    result = 0
    new_list = list()

    for step in range(list_length):
        try:
            result = my_list_1[step] / my_list_2[step]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)

    return (new_list)
