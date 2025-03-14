#!/usr/bin/python3


"""Function that returns a python object represented by a JSON string."""

import json


def from_json_string(my_str):
    """Return Python objects"""
    return json.loads(my_str)
