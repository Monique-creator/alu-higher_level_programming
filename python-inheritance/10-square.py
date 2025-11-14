#!/usr/bin/python3
"""
Module 10-square
Defines class Square that inherits from Rectangle
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise exception since area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize Square with validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

