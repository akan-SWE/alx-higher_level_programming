#!/usr/bin/python3

"""Implementations of the text_indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these
    characters: ., ? and :

    :param text: the text
    :return: None
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    line = ""
    for c in text:

        if c not in '.:?':
            # concatenate till the specified characters is encountered
            line += c
        else:
            line += c + '\n\n'
            print(line.strip(' '), end="")  # remove leading and trailing space
            line = ""  # begin a new line

    print(line.strip(' '), end="")  # last line
