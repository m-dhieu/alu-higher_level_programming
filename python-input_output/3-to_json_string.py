#!/usr/bin/python3


"""Function to convert object to JSON string representation."""


def to_json_string(my_obj):
    """Convert an object to its JSON string representation."""
    if isinstance(my_obj, dict):
        return dict_to_json(my_obj)
    elif isinstance(my_obj, list):
        return list_to_json(my_obj)
    elif isinstance(my_obj, str):
        return f'"{my_obj}"'
    elif isinstance(my_obj, bool):
        return "true" if my_obj else "false"
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    else:
        raise TypeError(f"Unsupported type for JSON serialization")


def dict_to_json(d):
    """Convert a dictionary to JSON string."""
    items = []
    for key, value in d.items():
        items.append(f'"{key}": {to_json_string(value)}')
    return "{" + ", ".join(items) + "}"


def list_to_json(lst):
    """Convert a list to JSON string."""
    items = [to_json_string(item) for item in lst]
    return "[" + ", ".join(items) + "]"
