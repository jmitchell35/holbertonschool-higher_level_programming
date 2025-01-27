#!/usr/bin/python3
"""
Module provides Square class
"""


class Square():
    """
    Simple Square class with initialization and area calculation methods
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
            raise TypeError ("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The square's area (size squared).

        Example:
            >>> square = Square(4)
            >>> square.area()
            16
        """
        return self.__size ** 2
