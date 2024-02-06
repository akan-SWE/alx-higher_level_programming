#!/usr/bin/python3
#
"""Defines Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Rectangle class

    Attribute:
        width (int): private attribute width
        height (int): private attribute height

    Methods:
        __init__: initialize width and height
        __str__: returns the following Rectangle description:
        [Rectangle] <width>/<height>

    """
    def __init__(self, width, height):

        self.integer_validator('width', width)  # validate width
        self.__width = width

        self.integer_validator('height', height)  # validate height
        self.__height = height

    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'

    def area(self):
        return self.__width * self.__height
