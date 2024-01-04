#!/usr/bin/python3


"""This module contains the Square class"""


class Square:
    """Defines a square class

    Attribute:
        size: size of the square
    Methods:
        __init__: initialize size and also verify the data
        area: returns the area of a square

    """
    def __init__(self, size=0):

        # verify size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
