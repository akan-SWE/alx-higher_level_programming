#!/usr/bin/python3

"""Defines MyList class"""


class MyList(list):
    """Creates a list, derived from the list class

    Methods:
        print_sorted: print a list in sorted order
    """
    def print_sorted(self):
        """sort the list and output the result"""
        self.sort()
        print(self)
