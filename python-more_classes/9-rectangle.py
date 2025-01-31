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
        number_of_instances: is such

    Raises:
        TypeError: If width or height is not an integer
        ValueError: If width or height is negative
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle with optional width and height.

        Args:
            width (int, optional): Width of rectangle. Defaults to 0.
            height (int, optional): Height of rectangle. Defaults to 0.

        Increments class counter number_of_instances
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        return '\n'.join(str(self.print_symbol) * self.width
                         for _ in range(self.height))\
            if self.width != 0 and self.height != 0 else ""

    def __del__(self):
        """
        Destructor method that prints a message when rectangle instance is
        deleted.

        Prints:
            str: "Bye rectangle..."

        Decrements class counter number_of_instances
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two Rectangle instances based on their areas and returns the
        larger one.

        Args:
            rect_1 (Rectangle): First rectangle to compare
            rect_2 (Rectangle): Second rectangle to compare

        Returns:
            Rectangle: The rectangle with the larger or equal area

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of
            Rectangle

        Example:
            >>> r1 = Rectangle(3, 4)  # area = 12
            >>> r2 = Rectangle(2, 5)  # area = 10
            >>> bigger = Rectangle.bigger_or_equal(r1, r2)
                >>> print(bigger)  # Will print r1 since 12 > 10
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a Rectangle instance with equal width and height, effectively
        making a square.
        This is a convenience class method that serves as an alternative
        constructor.

        Args:
            size (int, float): The length of each side of the square. Defaults
            to 0.

        Returns:
            Rectangle: A new Rectangle instance where width == height == size

        Example:
            >>> square = Rectangle.square(5)  # Creates a 5x5 square
            >>> print(square.width)  # 5
            >>> print(square.height)  # 5
            >>> print(square.area())  # 25

        Note:
            This method uses the class itself (cls) to instantiate a new
            object, making it inheritance-friendly as it will return an
            instance of any subclass that calls this method.
        """
        return cls(size, size)

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
