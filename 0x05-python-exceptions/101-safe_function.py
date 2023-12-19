#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """ Executes a function safely

    :param:
        fct: Pointer to the function
        args: Variadic parameters

    return: The result of the function called
    or None if an exception occurred
    """

    try:
        return fct(*args)
    except Exception as e:
        print('Exception:', e, file=sys.stderr)
        return None
