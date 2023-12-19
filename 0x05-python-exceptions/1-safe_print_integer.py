#!/usr/bin/python3

def safe_print_integer(value):
    """ Prints an integer

    :param value: The integer

    :return: True if value is correctly printed
    else False

    """
    try:
        print('{:d}'.format(value))
        return True
    except (ValueError, TypeError):
        return False
