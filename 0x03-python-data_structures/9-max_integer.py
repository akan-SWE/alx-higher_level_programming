#!/usr/bin/python3

def max_integer(my_list=[]):
    """ Find the biggest integer in a list

    :param my_list: the list

    :return: the biggest number, None otherwise

    """
    # list is empty
    if not len(my_list):
        return None

    max = my_list[0]  # initial max
    for num in my_list[1:]:
        # found a new greater number
        if num > max:
            max = num

    return max
