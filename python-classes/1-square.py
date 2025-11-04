#!/usr/bin/python3
"""This module defines a class Square that defines a square by its size."""


class Square:
    """This class represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square instance.
        
        Args:
            size: The size of the square (no type or value verification).
        """
        self.__size = size

