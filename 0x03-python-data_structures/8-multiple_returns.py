#!/usr/bin/python3

def multiple_returns(sentence):
    """ Returns the length of a string and the first character

    :param sentence: sentence to evaluate

    :return: length of a string and first character
    """
    # string is empty
    if not len(sentence):
        return len(sentence), None

    return len(sentence), sentence[0]
