#!/usr/bin/python3

"Defines the lookup function"


def lookup(obj):
    """returns the attributes and method of an object as a list"""
    return dir(obj)
