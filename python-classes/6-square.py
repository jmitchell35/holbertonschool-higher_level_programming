#!/usr/bin/python3
"""
Module providing simple Square class
"""


class Square:
    """
    Full Square class now completed.
    Methods : init, area, my print
    Properties and setters : size, position
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance.

        Args:
            size (int, optional): Length of square's side. Defaults to 0.
            position (tuple, optional): defines offset from left and top
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
        int: The length of the square's side.
        """
        return self.__size

    @property
    def position(self):
        """
        Get the offset for printing the square

        Returns:
        tuple: left and top offset
        """
        return self.__position

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
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Set square print offset from left and top

        Args:
            value(tuple): nb of ' ' (left margin) and '\n' (upper margin)
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """
        Print the square using # characters.

        Prints:
            Empty line if size is 0
            Square pattern of # characters otherwise

        Example:
            >>> square = Square(3)
            >>> square.my_print()
            ###
            ###
            ###
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
