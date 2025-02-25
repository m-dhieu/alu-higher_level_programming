#!/usr/bin/python3


def raise_exception():
    try:
        raise TypeError("This is a type error")
    except TypeError as e:
        print(f"Caught exception: {e}")
        raise

