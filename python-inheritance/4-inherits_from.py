#!/usr/bin/python3


"This module checks if instance is inherited from specified class."""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of a class inherited from specified class.
"""
    return isinstance(obj, a_class)
