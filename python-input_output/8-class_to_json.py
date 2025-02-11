#!/usr/bin/python3
"""Class to dictionary conversion module.

This module provides functionality to convert Class instances to dictionary
representation suitable for JSON serialization.
"""


def class_to_json(obj):
   """Convert a Class instance to a dictionary representation.

   Args:
       obj: Instance of a Class with serializable attributes.

   Returns:
       dict: Dictionary containing instance's attributes and values.

   Note:
       All attributes must be JSON serializable (dict, list, str, int, etc).
       Custom classes and complex objects like file handlers will fail.
   """
   return obj.__dict__  
   # would also work with vars(obj) as long as ev.t. is serializable