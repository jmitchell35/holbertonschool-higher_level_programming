#!/usr/bin/python3
"""
This module defines MyList class, which extends the built-in list class to add
sorted printing functionality.
"""


class MyList(list):
    """
   A custom list class that inherits from the built-in list class.
   Adds the ability to print elements in sorted order while maintaining the
   original list order.
   """
    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        The original list remains unmodified.

        Returns:
            None
        """
        print(sorted(self))
