#!/usr/bin/python3
"""
This module adds the matrix divided_function
"""


def matrix_divided(matrix, div):
    """
   Divides all elements of a matrix by a number and rounds to 2 decimal places.

   Args:
       matrix: List of lists containing integers or floats
       div: Number to divide matrix elements by (int or float)

   Returns:
       New matrix with elements divided by div, rounded to 2 decimal places

   Raises:
       TypeError: If matrix is not list of lists of numbers,
                 if rows have different sizes,
                 or if div is not a number
       ZeroDivisionError: If div is 0
   """
    if not div:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                "(list of lists) of integers/floats")
    new_matrix = []
    ref_row_len = 0
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix "
                    "(list of lists) of integers/floats")
        new_row = []
        if not ref_row_len:
            ref_row_len = len(row)
        else:
            if len(row) != ref_row_len:
                raise TypeError(
                        "Each row of the matrix must have the same size")
        for nb in row:
            if not isinstance(nb, (int, float)):
                raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
            new_row.append(float(f"{nb / div:.2f}"))
        new_matrix.append(new_row)
    return new_matrix
