#!/usr/bin/python3


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size):
        """
        Initialize a Square object.
        """
        self.__size = size

    def get_size(self):
        """
        Retrieve and return the size of the square.
        """
        return self.__size

    def set_size(self, value):
        """
        Set the size of the square.
        """
        self.__size = value
