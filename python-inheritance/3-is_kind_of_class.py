#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines a function that checks if an object is an instance of a class
or a class that inherited from it
"""

def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or its subclass,
    otherwise False
    """
    return isinstance(obj, a_class)

