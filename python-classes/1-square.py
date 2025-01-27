#!/usr/bin/python3
"""
Module provides the Square class
"""


class Square():
    """
    Simple class with __init__ method
    """
    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
        size: Length of square's side. Must be a non-negative integer.

        Returns:
        None

        Example:
        >>> square = Square(5)
        """
        self.__size = size
