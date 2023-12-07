#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ Adds 2 elements of two tuples together

    :param tuple_a: first tuple
    :param tuple_b: second tuple
    :return: the sum of two tuple
    """

    # ensure tuples are exactly 2 elements long
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return tuple_c
