#!/usr/bin/python3

"""pascal_triangle module"""


def pascal_triangle(n):
    """return a list of list that is a pascal triangle based on row n

    param:
        n: number of rows

    return: list of list representing a pascal triangle
    """
    row, prev_row, pascal_triangle = [], [], []

    if n < 1:
        return pascal_triangle

    for i in range(n):
        prev_num = 0
        for num in prev_row:
            sum = prev_num + num
            row.append(sum)
            prev_num = num
        row.append(1)
        pascal_triangle.append(row)
        prev_row = row
        row = []

    return pascal_triangle
