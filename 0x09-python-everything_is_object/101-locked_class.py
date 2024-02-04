#!/usr/bin/python3

"""Defines the LockedClass

Example:
    >>> lc = LockedClass()
    
    No error occurred when first_name is added dynamically
    >>> lc.first_name = "Snow"

    error occurred with other attribute names
    >>> lc.last_name = "White"
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'

"""
class LockedClass:
    """A class that does not have class or object attribute and can't be added dynamically
    except first_name

    Attribute:
        __slots__: The list contain only first_name
    """
    __slots__ = ["first_name"]