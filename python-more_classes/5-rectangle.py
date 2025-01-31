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

    def __repr__(self):
        """
        Return eval()-able string representation of Rectangle instance.

        Returns:
            str: Formatted string showing Rectangle class with width and
            height which can be eval() to create a Rectangle object
        """
        return f"Rectangle({self.width}, {self.height})"

    def __str__(self):
        """
        Return string visualization of rectangle using '#' characters.
        If width/height is 0, returns empty string.

        Returns:
            str: Rectangle pattern or empty string
        """
        return '\n'.join("#" * self.width for _ in range(self.height))\
            if self.width != 0 and self.height != 0 else ""

    def __del__(self):
        """
        Destructor method that prints a message when rectangle instance is
        deleted.

        Prints:
            str: "Bye rectangle..."
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The rectangle's width
        """
        return self.__width

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The rectangle's height
        """
        return self.__height

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
            raise ValueError("height must be >= 0")
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
            int: If width and height are non-zero: 2 * (width + height)
                    If either width or height is 0: returns 0
        """
        return 2 * (self.width + self.height) if self.width != 0 and \
            self.height != 0 else 0
