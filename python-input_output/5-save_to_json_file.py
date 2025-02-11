#!/usr/bin/python3
"""JSON file writing module.

This module provides functionality to write Python objects to a file in JSON
format using UTF-8 encoding.
"""
import json


def save_to_json_file(my_obj, filename):
   """Write Python object to a file in JSON format.

   Args:
       my_obj: Python object to serialize to JSON and write to file.
       filename (str): Path to the file to write to.

   Raises:
       TypeError: If object is not JSON serializable.
       IOError: If file cannot be opened or written to.
   """
   with open(filename, mode="w", encoding="utf-8") as f:
       f.write(json.dumps(my_obj))