#!/usr/bin/python3
"""
This module provides functionality to inspect Python objects by listing their
attributes and methods.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: Any Python object to inspect.

    Returns:
        list: A sorted list of strings, representing all the attributes and
        methods available to the object, including inherited ones.

    Example:
        >>> class MyClass:
        ...     pass
        >>> obj = MyClass()
        >>> lookup(obj)
        ['__class__', '__delattr__', '__dict__', '__dir__', ...]
    """
    return dir(obj)
