#!/usr/bin/python3

"""Defines MyList class"""


class MyList(list):
    """Creates a list, derived from the list class

    Methods:
        print_sorted: print a list in sorted order
    """
    def print_sorted(self):
        """sort the list, output the result and return a new list"""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
