#!/usr/bin/python3
"""JSON string parsing module.

This module provides functionality to parse JSON strings into their Python
object representation.
"""
import json


def from_json_string(my_str):
    """Convert a JSON string to its Python object representation.

    Args:
        my_str (str): JSON string to be converted.

    Returns:
        object: Python data structure (dict, list, str, int, etc).

    Raises:
        JSONDecodeError: If string is not a valid JSON.
        TypeError: If my_str is not a string.
    """
    return json.loads(my_str)