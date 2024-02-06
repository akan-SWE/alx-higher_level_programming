#!/usr/bin/python3

"""Define BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """Defines a geometry class

    Methods:
        area: currently raises an exception
        integer_validator: validates the object referenced by value
    """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates the object referenced by value"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
