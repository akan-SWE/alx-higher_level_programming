#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """ Deletes the item at a specific position

    :param my_list: The list
    :param idx: The position of the item in the list

    :return: New list without the item at @idx

    """
    if idx > len(my_list) or idx < 0:
        return my_list

    del my_list[idx:idx + 1]  # delete the item at this position

    return my_list
