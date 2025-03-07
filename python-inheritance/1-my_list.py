#!/usr/bin/python3


"""This module writes a class MyList that inherits from list."""


class MyList(list):
    """Represent MyList class."""

    def print_sorted(self):
        """Print list in ascending order."""
        print(sorted(self))
