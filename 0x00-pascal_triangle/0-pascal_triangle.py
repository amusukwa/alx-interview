#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """returns a list integers in pascal triangle"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            previous_row = triangle[i - 1]
            for j in range(1, i):
                element = previous_row[j - 1] + previous_row[j]
                row.append(element)
            row.append(1)
        triangle.append(row)

    return triangle
