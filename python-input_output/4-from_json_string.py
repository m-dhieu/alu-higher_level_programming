#!/usr/bin/python3


"""Function to parse a JSON string into a Python object."""


def from_json_string(my_str):
    """Convert a JSON string into a Python object."""
    my_str = my_str.replace("'", '"')
    
    try:
        return eval(my_str)
    except Exception as e:
        print(f"[JSONDecodeError] {str(e)}")
