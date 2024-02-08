#!/usr/bin/python3

"""Defines the write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file

    param:
        filename: the file name
        text: the text

    return:
        number of characters written to the file
    """

    with open(filename, mode='w', encoding='UTF-8') as fp:
        return fp.write(text)
