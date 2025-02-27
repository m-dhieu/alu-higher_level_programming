#!/usr/bin/python3


"""This module calculates the area of a square."""


class Square:
    """Represent a square of side length."""
    def __init__(self, size=0):
        """Initialize a Square object."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
