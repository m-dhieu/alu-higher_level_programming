#!/usr/bin/python3


"""This module writes a class that inherits from a list."""


class MyList(list):
    """Represent MyList class."""

    def print_sorted(self):
        """print sorted list."""
        print(sorted(self))
