#!/usr/bin/python3
"""
This module provides the rectangle class
"""


class Rectangle:
    """
    A class representing a rectangle with width and height attributes.

    Attributes:
        width (int): Width of the rectangle, must be non-negative
        height (int): Height of the rectangle, must be non-negative

    Raises:
        TypeError: If width or height is not an integer
        ValueError: If width or height is negative
    """
    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle with optional width and height.

        Args:
            width (int, optional): Width of rectangle. Defaults to 0.
            height (int, optional): Height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The rectangle's width
        """
        self.__width = width

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The rectangle's height
        """
        self.__height = height

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): New width value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): New height value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: Area as width * height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: Perimeter as 2 * (width + height)
        """
        return 2 * (self.width + self.height) if self.width != 0 and \
                self.height != 0 else 0
