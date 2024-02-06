#!/usr/bin/python3

"""Define the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns True if an object is an instance of, or the object is
    an instance of a class inherited from, the specified class;
    otherwise False"""
    return isinstance(obj, a_class)
