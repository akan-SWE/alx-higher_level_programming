#!/usr/bin/python3

def element_at(my_list, idx):

    """ Retrieves an element from a list

    :param my_list: The list
    :param idx: The index

    :return: The element at the index, otherwise None
    if index is greater than length of list or index a negative number
    """

    length = len(my_list)
    if idx >= length or idx < 0:
        return None

    return my_list[idx]
