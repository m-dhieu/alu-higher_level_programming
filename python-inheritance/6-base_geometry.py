#!/usr/bin/python3


"""This module writes a class with an exception message."""


class BaseGeometry:
    """A class BaseGeometry."""

    def area(self):
        """Raise an exception because area() is not implemented."""
        raise Exception("area() is not implemented")
