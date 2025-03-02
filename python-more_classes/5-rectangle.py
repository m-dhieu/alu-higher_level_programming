#!/usr/bin/python3


"""This module defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object with optional width and height."""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return string representation so a new instance is recreated."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
