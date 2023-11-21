#!/usr/bin/python3

def safe_print_division(a, b):
    """safe print division

    Args:
        a: the dividend
        b: the divisor

    Return:
        the quotient or the error
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
