#!/usr/bin/python3


"""
This module defines a square whose size must be an integer, otherwise a TypeError is raised. A ValueError is raised if it is less than zero.
"""


class Square:
    """
    Represent a square with a given side length.
    """
    def __init__(self, size=0):
        """
        Initialize a Square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
