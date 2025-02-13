#!/usr/bin/python3
"""
Pascal Triangle Generator Module

This module provides functionality to generate Pascal's Triangle, a triangular
array of binomial coefficients where each number is the sum of the two numbers
directly above it.

Example:
    >>> triangle = pascal_triangle(4)
    >>> print(triangle)
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1]
    ]
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with the specified number of rows.

    Args:
        n (int): Number of rows to generate. Must be non-negative.

    Returns:
        list: A list of lists representing Pascal's Triangle.
              Each inner list represents one row of the triangle.
              Returns empty list if n <= 0.

    Example:
        >>> pascal_triangle(3)
        [[1], [1, 1], [1, 2, 1]]
        >>> pascal_triangle(0)
        []

    Note:
        - Time complexity: O(n²)
        - Space complexity: O(n²)
        - The first row is [1]
        - Each subsequent number is the sum of the two numbers above it
        - Each row starts and ends with 1
    """
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                value = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(value)
        triangle.append(current_row)
    return triangle
