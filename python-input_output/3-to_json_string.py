#!/usr/bin/python3
"""JSON string conversion module.

This module provides functionality to convert Python objects to their JSON
string representation.
"""
import json


def to_json_string(my_obj):
    """Convert a Python object to its JSON string representation.

    Args:
        my_obj: Python object to be converted to JSON string.

    Returns:
        str: JSON string representation of the object.

    Raises:
        TypeError: If object is not JSON serializable.
    """
    return json.dumps(my_obj)
