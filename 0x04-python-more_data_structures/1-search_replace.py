#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ Replaces all occurrences of an element by another in a new list.

    :param my_list: The initial list
    :param search: The element to replace in the list
    :param replace: The new eleent

    :return: A list that has replaced any occurrence of @search by @replace
    """
    return [replace if search == i else i for i in my_list]
