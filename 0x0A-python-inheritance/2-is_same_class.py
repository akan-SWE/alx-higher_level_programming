#!/usr/bin/python3

"""Define function is_same_class"""


def is_same_class(obj, a_class):
    """returns True if an object is exactly an instance of the
    specified classs"""
    return True if type(obj) is a_class else False
