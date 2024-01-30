#!/usr/bin/python3

"""Defines the lazy_matrix_mul function"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Uses the numpy module to calculate the multiplication of two matrix

    Args:
        m_a (list): the first matrix
        m_b (list): the second matrix

    Raises: numerous errors on different edge cases

    Returns: an array containing the result of the multiplied matrices
    """

    # check if the list is empty
    if not len(m_a):
        raise ValueError("m_a can't be empty")
    elif not len(m_b):
        raise ValueError("m_b can't be empty")

    A, B = np.array(m_a), np.array(m_b)

    return np.matmul(A, B)
