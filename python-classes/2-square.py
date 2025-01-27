#!/usr/bin/python3
"""
Module provides the Square class
"""


class Square:
    """
    Simple Square class with initialization method including value verif
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance with input validation.

        Args:
        size (int, optional): Length of square's side. Defaults to 0.

        Raises:
        TypeError: If size is not an integer or is negative.

        Example:
        >>> square = Square(5)  # Valid
        >>> square = Square(-1) # Raises TypeError
        >>> square = Square("5") # Raises TypeError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
