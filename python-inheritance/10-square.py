#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
It implements a simple geometric square with size validation.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    This class extends Rectangle to implement specific square functionality,
    where width and height are equal (size).
    """
    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square (both width and height).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self, size):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
