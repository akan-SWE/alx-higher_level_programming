#!/usr/bin/python3


"""This module contains the Square class"""


class Square:
    """Defines a square class

    Attribute:
        size: size of the square
    Methods:
        __init__: initialize size and also verify the data
        area: returns the area of a square

    Property:
        size (getter): Get the current size of the square
        size (setter): Set the current size of the square

    """
    def __init__(self, size=0):
        self.size = size  # call the (setter) size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
