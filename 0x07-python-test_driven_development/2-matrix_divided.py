#!/usr/bin/python3

"""Defines matrix_divided and some other functions

    Functions:
        matrix_divided: divides a matrix by a divisor
        check_element_type: check if the element in the list is a number
        check_type: checks if it is a list of list
        check_size: checks if all the row in the matrix have equal size
"""


def check_element_type(matrix):
    """checks if the element in the matrix is a number if not raises
    TypeError
    :param
        matrix: the matrix
    :return void
        """
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')


def check_type(matrix):
    """checks if the matrix is a list of lists, otherwise raises a TypeError
    :param
        matrix: the matrix
    :return void
        """
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    else:
        if not (all(isinstance(row, list) for row in matrix)):
            raise TypeError('matrix must be a matrix (list of lists)'
                            ' of integers/floats')


def check_size(matrix):
    """checks if the rows are equal throughout the matrix, otherwise raises
    TypeError
    :param
        matrix: the matrix
    :return void
        """
    initial_size = len(matrix[0])
    if not all(len(row) == initial_size for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')


def matrix_divided(matrix, div):
    """Divides a matrix by @div
    :param
        matrix: the matrix
        div: the divisor
    return:
        a new matrix
    """
    check_type(matrix), check_element_type(matrix), check_size(matrix)
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    elif not div:
        raise ZeroDivisionError('division by zero')

    return [[round(j / div, 2) for j in i] for i in matrix]
