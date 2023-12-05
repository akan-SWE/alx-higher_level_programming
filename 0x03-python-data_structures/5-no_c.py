#!/usr/bin/python3

def no_c(my_string):
    """ Removes all characters c and C from a string

    :param:
        my_string: The string

    :return:
        The new string that contains characters without
        c or C

    """
    new_string = ''
    for char in my_string:

        if char == 'c' or char == 'C':
            continue

        new_string += char  # append characters

    return new_string
