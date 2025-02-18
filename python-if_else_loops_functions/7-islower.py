#!/usr/bin/python3
def islower(c):
    return ord(c) >= 97 and ord(c) <= 122

def islower(c):
    """
    Check for lowercase character.

    Prototype: def islower(c):
    Returns True if c is lowercase
    Returns False otherwise
    """
    return 97 <= ord(c) <= 122
