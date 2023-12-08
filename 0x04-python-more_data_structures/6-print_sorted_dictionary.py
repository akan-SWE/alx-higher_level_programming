#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """ Prints a dictionary by ordered keys

    :param a_dictionary: The dictionary

    :return: void (Nothing)

    """
    keys = list(a_dictionary.keys())  # get keys

    keys.sort()  # sort list

    # output ordered key : value
    for key in keys:
        print('{}: {}'.format(key, a_dictionary[key]))
