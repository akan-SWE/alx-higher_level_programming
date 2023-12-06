#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    """ Prints a matrix of integers

    :param:
        matrix: The matrix
    :return:
        void (Nothing)

    """
    for row in matrix:
        print(' '.join("{:d}".format(cell) for cell in row))
