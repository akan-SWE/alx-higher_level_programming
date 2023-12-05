#!/bin/python3

def new_in_list(my_list, idx, element):

    """ Replaces an element at a specific position without modifying
    the origin list

    :param my_list: The list
    :param idx: The index
    :param element: The element

    :return: The new list that contains the element or a copy
    of the original list if the function fails
    """

    copy_list = my_list.copy()  # get a copy

    if idx >= len(copy_list) or idx < 0:
        return copy_list

    copy_list[idx] = element  # replace

    return copy_list
