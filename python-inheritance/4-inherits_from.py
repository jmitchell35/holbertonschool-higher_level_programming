#!/usr/bin/python3
"""
This module provides a function to check if an object is an inherited instance
of a class.
"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an inherited instance of a class.
    Returns True if the object is an instance of a class that inherited from
    the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj inherits from a_class (directly or indirectly),
              False otherwise.

    Example:
        >>> class Parent: pass
        >>> class Child(Parent): pass
        >>> c = Child()
        >>> inherits_from(c, Parent)
        True
        >>> inherits_from(c, Child)
        False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
