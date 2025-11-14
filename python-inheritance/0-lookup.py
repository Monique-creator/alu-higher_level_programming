#!/usr/bin/python3
"""
Module 0-lookup
Defines a function that returns the list of attributes and methods of an object
"""

def lookup(obj):
    """Return list of available attributes and methods of an object"""
    return dir(obj)

