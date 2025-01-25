#!/usr/bin/python3
"""
Module providing the print-square function
"""


def print_square(size):
    """
    Prints a square made of '#' characters with input validation.

    Args:
        size: The side length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is negative

    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
