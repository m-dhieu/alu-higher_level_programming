#!/usr/bin/python3


"""This module defines a Square class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent Square."""

    def __init__(self, size):
        """Initialize square with a given size."""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation of square."""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Calculate and return area of square."""
        return self.__size ** 2
