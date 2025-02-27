#!/usr/bin/python3


"""This module compares 2 squares."""


class Square:
    """Represent a Square."""
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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.size ** 2

    def __eq__(self, other):
        """Check if 2 squares are = based on their areas."""
        if not isinstance(other, Square):
            return False
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if 2 squares are != based on their areas."""
        return not self == other

    def __gt__(self, other):
        """Check if a square is > another based on their areas."""
        if not isinstance(other, Square):
            raise TypeError("Unsupported operand type for >")
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if a square is > or = to another based on their areas."""
        if not isinstance(other, Square):
            raise TypeError("Unsupported operand type for >=")
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if a square is < another based on their areas."""
        if not isinstance(other, Square):
            raise TypeError("Unsupported operand type for <")
        return self.area() < other.area()

    def __le__(self, other):
        """Check if a square is < or = to another based on their areas."""
        if not isinstance(other, Square):
            raise TypeError("Unsupported operand type for <=")
        return self.area() <= other.area()
