#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle with width and height"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height

        Args:
            width (int): The width of the rectangle (default 0)
            height (int): The height of the rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width attribute

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute

        Args:
            value (int): The new width value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute

        Args:
            value (int): The new height value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle with # characters

        Returns:
            str: The rectangle drawn with # characters, empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rectangle_str = []
        for i in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Return string representation to recreate the rectangle

        Returns:
            str: String that can be used with eval() to recreate the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor that prints a message when the rectangle is deleted"""
        print("Bye rectangle...")
