#!/usr/bin/python3

def safe_print_integer(value):
    """safe print integer

    Args:
        value: the value must be int

    Returns:
        return TRUE and otherwise FAlSE
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return (False)
    else:
        return (True)
