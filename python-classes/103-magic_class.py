#!/usr/bin/python3


"""This module defines a MagicClass that does specific ByteCode."""


class MagicClass:
    """Represent a MagicClass."""
    def __init__(self, radius=0):
        """Initialize a MagicClass object."""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle."""
        PI = 3.141592653589793  # Constant for pi
        return self.__radius ** 2 * PI

    def circumference(self):
        """Calculate the circumference of the circle."""
        PI = 3.141592653589793  # Constant for pi
        return 2 * PI * self.__radius
