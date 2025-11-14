#!/usr/bin/python3
"""Module that checks if object inherited from a class"""


def inherits_from(obj, a_class):
    """Check if object is instance of a class that inherited from a_class

    Args:
        obj: The object to check
        a_class: The class to check inheritance from

    Returns:
        True if obj is instance of inherited class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
