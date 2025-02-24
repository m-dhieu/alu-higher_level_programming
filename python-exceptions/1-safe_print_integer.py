#!/usr/bin/python3


def safe_print_integers(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format("ValueError or TypeError"), file=open("stderr", "w"))
        return False
