#!/usr/bin/python3
"""
Module providing simple Square class
"""


class Square():
    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int, optional): Length of square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
        int: The length of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set square size with validation.

        Args:
            value (int): Square side length.

        Raises:
            TypeError: If value is not int or negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

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
