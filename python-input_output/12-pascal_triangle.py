#!/usr/bin/python3
"""
Module for generating Pascal's Triangle.

This module provides functionality to generate Pascal's Triangle
up to a specified number of rows.
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal's triangle of n.

    Pascal's triangle is a triangular array where each number is the sum
    of the two numbers directly above it. The triangle starts with 1 at
    the top, and each row begins and ends with 1.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists where each inner list represents a row
              in Pascal's triangle. Returns an empty list if n <= 0.

    Example:
        >>> triangle = pascal_triangle(5)
        >>> for row in triangle:
        ...     print(row)
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
        [1, 4, 6, 4, 1]
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        triangle.append(row)

    return triangle
