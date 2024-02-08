#!/usr/bin/python3

"""Defines save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file, using JSON representation

    param:
        my_obj: the object
        filename: text file

    returns: number of text written to the file
    """
    with open(filename, mode='w', encoding='UTF-8') as fp:
        return fp.write(json.dumps(my_obj))
