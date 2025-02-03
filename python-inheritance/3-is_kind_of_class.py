#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or if it inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Determines if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclasses,
              False otherwise.

    Example:
        >>> is_kind_of_class(1, int)
        True
        >>> is_kind_of_class(1, object)
        True
        >>> is_kind_of_class(1, float)
        False
    """
    return isinstance(obj, a_class)
