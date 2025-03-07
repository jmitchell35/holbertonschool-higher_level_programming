#!/usr/bin/python3
"""
Text Indentation Module

This module provides functionality to format text by adding newlines
after specific punctuation marks (., ?, :). It processes the input
text and adds two newlines after each specified separator.
"""


def text_indentation(text):
    """
    Format text by adding double newlines after specific punctuation.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text argument is not a string.

    Examples:
        >>> text_indentation("Hello. How are you? I am good: Thanks.")
        Hello.

        How are you?

        I am good:

        Thanks.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()  # Remove leading/trailing char, default whitespace
    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n\n", end="")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
