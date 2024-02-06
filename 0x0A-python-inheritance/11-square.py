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

        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f'[Square] {self._Rectangle__width}/{self._Rectangle__height}'
