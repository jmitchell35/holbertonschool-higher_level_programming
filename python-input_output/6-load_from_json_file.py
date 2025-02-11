#!/usr/bin/python3
"""JSON file reading module.

This module provides functionality to read JSON formatted files and convert
their content to Python objects.
"""
import json


def load_from_json_file(filename):
   """Create Python object from JSON file.

   Args:
       filename (str): Path to the JSON file to read from.

   Returns:
       object: Python data structure representing the JSON content.

   Raises:
       FileNotFoundError: If file does not exist.
       JSONDecodeError: If file content is not valid JSON.
       IOError: If file cannot be opened or read.
   """
   with open(filename, mode="r", encoding="utf-8") as f:
       object = json.loads(f.read())
   return object