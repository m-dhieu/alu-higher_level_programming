#!/usr/bin/python3


"""This module provides a function to append text to a file.
The number of characters added should be returned."""


def append_write(filename="", text=""):
    """Append string to UTF-8 text file and return number of characters added.

    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
