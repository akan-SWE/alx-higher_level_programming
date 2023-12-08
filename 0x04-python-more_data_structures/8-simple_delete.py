#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """ Deletes a key in dictionary

    :param a_dictionary: The dictionary
    :param key: The key to delete

    :return: The updated dictionary that is without key if available
    or dictionary with updating if key is not available.
    """
    # only delete when key is present
    if key in a_dictionary.keys():
        a_dictionary.pop(key)

    return a_dictionary
