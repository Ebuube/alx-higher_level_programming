#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list
    Args:
        my_list: can contain any type (integer, string, etc.)
        x: number of the elements to print

    Returns:
        The real number of elements printed
    """
    count = 0
    for count in range(x):
        try:
            print(my_list[count], end='')
            count += 1
        except IndexError:
            break
        except TypeError:
            break

    print()
    return (count)
