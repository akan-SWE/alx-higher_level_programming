#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ Prints x element of a list

    :param my_list: The list
    :param x: Number of element to print

    :return: Number of element that was outputted
    """
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
        except IndexError:
            break
        i += 1

    print()
    return i
