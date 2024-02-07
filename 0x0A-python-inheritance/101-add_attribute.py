#!/usr/bin/python3

"""Define add_attribute function"""


def add_attribute(obj, name, value):
    """Adds attribute to an object, raises an error if it can't

    params:
        obj (any type): the object
        name (str): the name of the attribute
        value (any type): the value to assign to the attribute

    """
    # if __dict__ attribute is not present means attribute can't be added
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
