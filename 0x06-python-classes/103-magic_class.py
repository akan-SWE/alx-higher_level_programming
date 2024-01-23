#!/usr/bin/python3
"""Wrote the MagicClass class from the bytecode provided from task 10"""

import math


class MagicClass:
    """Defines a circle class
    Attribute:
        radius: The radius of the circle object with a private access modifier
    Methods:
        __init__(): initializes the radius of the circle and checks if the
                    number passed is exactly an integer or a float
        area(): area of the circle
        circumference: circumference of a circle
    """
    def __init__(self, radius=0):
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
