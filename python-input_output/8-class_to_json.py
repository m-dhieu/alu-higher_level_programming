#!/usr/bin/python3


"""Function to convert an object to a dictionary for JSON serialization."""


def class_to_json(obj):
    """Convert an object to a dictionary for JSON serialization."""
    obj_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[attr] = value
    return obj_dict
