#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """Defines a Rectangle class

    Attribute:
        height (int): height of the Rectangle
        width (int): width of the Rectangle

    Properties:
        height (setter and getter): set and get the height of the Rectangle
        width (setter and getter): set and get the width of the Rectangle

    Methods:
        area: area of the Rectangle (h * w)
        perimeter: perimeter of the Rectangle 2(h + w)
        str: returns the string representable of the Rectangle object
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        # if width or height is equal to 0, perimeter is equal to 0
        return 0 if not self.width or not self.height \
            else 2 * (self.height + self.width)

    def __str__(self):
        # if width or height is equal to 0, return an empty string
        return "" if not self.width or not self.height \
            else ('#' * self.width + '\n') * self.height

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value
