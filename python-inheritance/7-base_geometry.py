#!/usr/bin/python3
"""
This module defines a base class for geometric shapes.
"""


class BaseGeometry:
    """
    A base class that serves as a template for geometric shape classes.
    This class is currently empty and meant to be extended by other classes
    that will implement specific geometric calculations and properties.
    """
    def area(self):
        """
        Calculates the area of a geometric shape.

        Raises:
            Exception: Always raises an Exception with message
                      "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.

        Example:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("side_length", 5)  # Valid
            >>> bg.integer_validator("radius", -3)  # Raises ValueError
            >>> bg.integer_validator("age", "20")  # Raises TypeError
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
