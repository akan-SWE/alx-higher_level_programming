#!/usr/bin/python3

"""Defines to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object string

    param:
        my_obj: the object

    returns: JSON representation of an object string
    """
    return json.dumps(my_obj)
