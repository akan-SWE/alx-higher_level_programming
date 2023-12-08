#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ Adds all unique integers in a list

    :param my_list: The list

    :return: sum of all unique integers in the list

    """
    to_set = set(my_list)  # make all integers unique

    add = 0
    for item in to_set:  # add all unique integers
        add += item

    return add
