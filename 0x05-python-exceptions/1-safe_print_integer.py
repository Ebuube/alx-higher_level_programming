#!/usr/bin/python3

def safe_print_integer(value):
    """A function that safely prints an integer with `"{:d}".format().`
    Args:
        value: an type of value

    Returns:
        True if integer is printed else Fals
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return (False)

    return (True)
