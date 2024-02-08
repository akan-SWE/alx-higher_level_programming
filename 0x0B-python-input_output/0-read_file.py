#!/usr/bin/python3

"""Defines the read_file function"""


def read_file(filename=""):
    """ Reads text from a file

    param:
        filename: name of the file
    """
    with open(filename, encoding='UTF-8') as fp:
        print(fp.read(), end="")
