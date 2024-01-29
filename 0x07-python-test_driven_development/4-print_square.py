#!/usr/bin/python3

"""Defines the print_square function"""


def print_square(size):
    """print_square: prints a square
    :param
        size: size of the square
    :return None
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    # when size is 0
    if size != 0:
        print((('#' * size + '\n') * size)[:-1])
