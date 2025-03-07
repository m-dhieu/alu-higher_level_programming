#!/usr/bin/python3


"""This module checks for a subclass or instance."""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance or subclass of a specified class.
    """
    return isinstance(obj, a_class)
