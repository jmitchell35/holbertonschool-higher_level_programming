#!/usr/bin/python3
"""
File Reader Module

This module provides functionality for reading and displaying text file contents.
Supports UTF-8 encoded files.

Functions:
   read_file: Reads and prints contents of a text file to stdout

Usage:
   from file_reader import read_file
   read_file("example.txt")
"""


def read_file(filename=""):
    """
   Reads and prints the contents of a text file to stdout.

   Args:
       filename (str): Path to the file to be read. Defaults to empty string.

   Raises:
       FileNotFoundError: If the specified file does not exist
       PermissionError: If the program lacks read permissions for the file
       UnicodeDecodeError: If the file cannot be decoded using UTF-8 encoding
   """
    with open(filename, encoding="utf-8") as f:
        print(f.read())