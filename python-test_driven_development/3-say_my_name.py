#!/usr/bin/python3
"""
Module provides say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted name string using the provided first and optional last name.

    Args:
        first_name (str): The first name to display. Must be a non-empty string.
        last_name (str, optional): The last name to display. Defaults to empty string.

    Raises:
        TypeError: If first_name or last_name is not a string, or if first_name is empty.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe
        >>> say_my_name("Jane")
        My name is Jane
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "":
        raise TypeError("non-empty first_name is required")

    print("My name is {} {}".format(first_name, last_name))
