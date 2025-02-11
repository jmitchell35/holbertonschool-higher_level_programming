#!/usr/bin/python3
"""File I/O Module.

This module provides functionality for writing text content to files using
UTF-8 encoding.
"""


def write_file(filename="", text=""):
    """Write string to a text file (UTF-8) and return chars written.

    Args:
        filename (str, optional): Path to the file. Defaults to empty string.
        text (str, optional): Content to write. Defaults to empty string.

    Returns:
        int: Number of characters written to the file.

    Raises:
        IOError: If file cannot be opened or written to.
        TypeError: If filename or text are not strings.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        nb_of_char = f.write(text)
    
    return (nb_of_char)