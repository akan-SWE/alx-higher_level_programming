#!/usr/bin/python3
"""Defines the Square class

Classes:
        Square: Defines a square
Example:
        To use this module import the Square class and create an instance
        ```python
        from models.square import Square

        s = Square()
        ```
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a square

    Attributes:
        id (int): A unique identifier to each instance
        width (int): width of the square
        height (int): height of the square
        x (int): x
        y (int): y

    Methods:
        __init__: initalize the new instance of the Square class
        __str__: returns the square in the format
                [Square] (<id>) <x>/<y> - <size>
        display: outputs the representation of square using the character #

    Properties:
        width (setter and getter): set and get the width of the square
        height (setter and getter): set and get the height of the square

    Example:
    >>> s = Square(3)
    >>> print(s.id)
    1
    """
    def __init__(self, size, x=0, y=0, id=None):
        # initialize the rectangle class
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
