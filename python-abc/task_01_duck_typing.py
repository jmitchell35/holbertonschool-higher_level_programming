#!/usr/bin/env python3
"""Geometric shapes module providing abstract Shape class and concrete
implementations.

This module defines an abstract base class for shapes and implements common
geometric shapes like Circle and Rectangle. Each shape provides methods to
calculate its area and perimeter.

Classes:
    Shape: Abstract base class defining the interface for geometric shapes
    Circle: Implementation of a circle shape
    Rectangle: Implementation of a rectangle shape

Functions:
    shape_info: Utility function to print shape measurements
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for geometric shapes."""
    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape
        """
        pass


class Circle(Shape):
    """A circle shape defined by its radius."""
    def __init__(self, radius):
        """Initialize a circle.

        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius

    def area(self):
        """Calculate the circle's area using πr².

        Returns:
            float: The area of the circle
        """
        return abs(pi * (self.radius**2))

    def perimeter(self):
        """Calculate the circle's circumference using 2πr.

        Returns:
            float: The circumference of the circle
        """
        return abs(2 * pi * self.radius)


class Rectangle(Shape):
    """A rectangle shape defined by width and height."""
    def __init__(self, width, height):
        """Initialize a rectangle.

        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the rectangle's area using width × height.

        Returns:
            float: The area of the rectangle
        """
        return abs(self.width * self.height)

    def perimeter(self):
        """Calculate the rectangle's perimeter using 2(width + height).

        Returns:
            float: The perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a given shape.
    Args:
        shape (Shape): A shape object implementing the Shape interface
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
