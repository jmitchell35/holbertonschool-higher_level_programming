#!/usr/bin/python3
"""Student class module.

This module defines a Student class with basic attributes and a method to
convert instance to JSON-compatible dictionary format.
"""


class Student:
    """Class representing a student.

    A simple student class with basic personal information that can be
    converted to a JSON-compatible dictionary format.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert Student instance to dictionary representation.

            Args:
                attrs (list, optional): List of strings representing attribute
                names to retrieve. If None, all attributes are retrieved.

            Returns:
                dict: Dictionary containing selected instance attributes,
                sorted by key length. Only existing attributes are included.
        """
        if isinstance(attrs, list) and all((
                isinstance(item, str) for item in attrs)):
            dict_to_return = {i: self.__dict__.get(i)
                              for i in attrs if self.__dict__.get(i)}
        else:
            dict_to_return = self.__dict__

        return dict(sorted(dict_to_return.items(), key=lambda x: len(x[0])))
