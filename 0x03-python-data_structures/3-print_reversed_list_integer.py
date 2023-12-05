#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    """ Prints a list in reversed other

    :param my_list: The list

    :return: void (Nothing

    """
    if my_list is not None:
        copy = my_list[:]  # get a copy

        copy.reverse()  # reverse the list
        for integer in copy:
            print('{:d}'.format(integer))
