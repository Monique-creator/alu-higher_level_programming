#!/usr/bin/python3
"""
Module 11-student
Defines a class Student with JSON serialization and deserialization methods
"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes in this list
        are retrieved. Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        using a dictionary (json).
        """
        for key, value in json.items():
            setattr(self, key, value)

