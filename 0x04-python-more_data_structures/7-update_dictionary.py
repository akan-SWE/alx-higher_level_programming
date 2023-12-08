#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """ Replaces or adds key/value in a dictionary

    :param a_dictionary: The dictionary
    :param key: The key
    :param value: The value

    :return: An updated dictionary
    """
    a_dictionary.update({key: value})
    return a_dictionary
