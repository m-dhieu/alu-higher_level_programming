#!/usr/bin/python3


"""Function to create an object from a JSON file."""


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return eval(f.read())
