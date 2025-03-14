#!/usr/bin/python3


"""This module provides a function to write text to a file.
The number of characters written should be returned."""


def write_file(filename="", text=""):
    """Write string to UTF-8 text file and return number of characters written

    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
