#!/usr/bin/python3

"""Define Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square

    Methods:
        __init__: initialize the size of the Square
        __str__: returns the following Rectangle description:
        [Rectangle] <width>/<height>
       """

    def __init__(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        super().__init__(size, size)
