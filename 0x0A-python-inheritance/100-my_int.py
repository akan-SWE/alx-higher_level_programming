#!/usr/bin/python

"""Define MyInt class"""


class MyInt(int):

    """MyInt is a subclass to the int class and it inverts the
    == and != operators when used

    Methods:
        __eq__: returns the inverse of == which is !=
        __ne__: returns the inverse of != which is ==
    """
    def __eq__(self, other):
        return not (super().__eq__(other))

    def __ne__(self, other):
        return not (super().__ne__(other))
