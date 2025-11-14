#!/usr/bin/python3
"""
Module 8-class_to_json
Defines a function that returns the dictionary description for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure
    for JSON serialization of an object
    """
    return obj.__dict__

