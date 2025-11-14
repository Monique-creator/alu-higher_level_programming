#!/usr/bin/python3
"""Module that defines a Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a square with size
        
        Args:
            size: the size of the square (width and height)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square
        
        Returns:
            The area of the square (size * size)
        """
        return self.__size * self.__size

    def __str__(self):
        """Return string representation of the square
        
        Returns:
            String in format [Square] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"
