#!/usr/bin/python3i
"""
This module provides a function to check if an object is exactly an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Determines if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.

    Example:
        >>> is_same_class(1, int)
        True
        >>> is_same_class(1.0, int)
        False
        >>> is_same_class(1, object)
        False
    """
    return type(obj) is a_class
