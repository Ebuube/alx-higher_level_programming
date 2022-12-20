#!/usr/bin/python3

def safe_print_division(a, b):
    """Assumig a and b are integers, this function divides a by b

    Args:
        a: integer
        b: integer
    Returns:
        The reult of the division else None
    """
    result = float()
    try:
        result = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        return (None)
    finally:
        print("Inside result: {}".format(result))

    return (result)
