#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """A function that executest a function safely

    Args:
        fct: a pointer to a function
        args: args to the function pointed to by fct

    Returns:
        The result of the function elses None if something happens
    """
    result = 0
    try:
        result = fct(args)
    except Exception as e:
        print("Exception: " + str(e), file=sys.stderr)
        return (None)

    return (result)
