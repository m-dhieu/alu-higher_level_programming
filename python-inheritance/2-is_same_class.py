#!/usr/bin/python3


"""This module writes a function that checks if instance is inherited."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class."""
    return type(obj) == a_class
