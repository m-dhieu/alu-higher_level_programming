#!/usr/bin/python3

"""This module defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a Square object."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square to stdout.
        If size is zero, print an empty line."""
        if self.size == 0:
            print()  # Print newline
            return

        for _ in range(self.size):
            print("#" * self.size)
