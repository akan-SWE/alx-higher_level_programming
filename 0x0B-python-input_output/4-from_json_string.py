#!/usr/bin/python3

"""Defines from_json_string function"""
import json


def from_json_string(my_obj):
    """Returns an object

    param:
        my_obj: JSON data set

    returns: an object
    """
    return json.loads(my_obj)
