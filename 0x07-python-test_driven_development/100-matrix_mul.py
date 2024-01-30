#!/usr/bin/python3

def all_num(matrix, name):
    """checks if the element in the matrix is a number if not raises
    TypeError
    :param
        matrix: the matrix
    :return void
        """
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(f'{name} should contain only integers '
                                f'or floats')


def check_type(m_a, m_b):

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')


def is_empty(m_a, m_b):
    if not len(m_a):
        raise ValueError("m_a can't be empty")
    elif not len(m_b):
        raise ValueError("m_b can't be empty")


def is_equal_size(m_a, m_b):
    initial_size1, initial_size2 = len(m_a[0]), len(m_b[0])

    if not all(len(row) == initial_size1 for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    elif not all(len(row) == initial_size2 for row in m_b):
        raise TypeError('each row of m_b must be of the same size')


def check_compatibility(m_a, m_b):
    col, row = len(m_a[0]), len(m_b)

    if col != row:
        raise ValueError("m_a and m_b can't be multiplied")


def matrix_mul(m_a, m_b):
    check_type(m_a, m_b), is_empty(m_a, m_b)
    all_num(m_a, 'm_a'), all_num(m_b, 'm_b')
    is_equal_size(m_a, m_b)
    check_compatibility(m_a, m_b)

    result = 0
    row = []
    matrix_mul_result = []
    for i in range(len(m_a)):  # iterate over the row
        for j in range(len(m_b[0])):  # iterate over the column:
            # iterate over each element in the column
            for k in range(len(m_b)):
                result += m_a[i][k] * m_b[k][j]

            row.append(result)
            result = 0
        matrix_mul_result.append(row)
        row = []

    return matrix_mul_result
