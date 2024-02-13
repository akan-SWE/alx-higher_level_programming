#!/usr/bin/python3
"""Defines the Rectangle class

Classes:
        Rectangle: Defines a rectangle
Example:
        To use this module import the Base class and create an instance
        ```python
        from models.rectangle import Rectangle

        r = Rectangle()
        ```
"""
from models.base import Base


class Rectangle(Base):
    """ Defines a rectangle

    Attributes:
        id (int): A unique identifier to each instance
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x
        y (int): y

    Methods:
        __init__: initalize the new instance of the Rectangle class

    Properties:
        width (setter and getter): set and get the width of the rectangle
        height (setter and getter): set and get the height of the rectangle

    Example:
    >>> base = Base()
    >>> print(base.id)
    1
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
