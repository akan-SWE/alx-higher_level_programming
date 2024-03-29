#!/usr/bin/python3
"""say_my_name: A function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """say_my_name: A function that prints My name is <first name> <last name>

    :param first_name, last_name

    :return: None
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
