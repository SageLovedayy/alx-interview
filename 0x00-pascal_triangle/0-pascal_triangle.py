#!/usr/bin/python3

"""
pascal_triangle - This function returns a list of integers representing
the Pascal's triangle of n.

This function assumes that n would always be an integer

We will need a list of lists. This would be the triangle itself.
Each list withing the triangle would represent a row

First, we will need to define an empty triangle and iteratively
populate the appropriate rows that would be empty on declaration

Also, the step above should only be used when n is not less than
or equal to 0. If this is the case, we would return an empty array
"""


def pascal_triangle(n):
    """Returns a list of lists representation of the triangle"""

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
