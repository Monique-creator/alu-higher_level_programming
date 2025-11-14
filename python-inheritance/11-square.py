#!/usr/bin/python3
"""
Module 11-square
Defines class Square with __str__ method
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize Square with validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return square description"""
        return f"[Square] {self.__size}/{self.__size}"

