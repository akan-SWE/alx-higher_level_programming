#!/usr/bin/python3

"""Defines load_from_json_file"""
import json


def load_from_json_file(filename):
    """ Creates an object from a JSON file

    param:
        filename: the name of the file

    returns: returns the newly created object
    """
    with open(filename, encoding='UTF-8') as fp:
        return json.loads(fp.read())
