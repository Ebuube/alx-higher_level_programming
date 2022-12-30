#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """A function that prints an integer

    Args:
        value: An object of anytype

    Returns:
        True on Success
        Else False

    Note:
        If 'value' is not an integer, "False" is sent to stderr
    """

    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception: " + str(ve), file=sys.stderr)
        return (False)
    except TypeError as te:
        print("Exception: " + str(te), file=sys.stderr)
        return (False)

    return (True)
