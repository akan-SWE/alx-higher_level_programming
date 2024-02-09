#!/usr/bin/python3

"""class_to_json module
"""


def class_to_json(obj):
    """Dictionary description with simple data structure

    param:
        obj: class instance

    return: dictionary description with simple data structure
    """
    return obj.__dict__
