#!/usr/bin/python3


def safe_print_integers(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError):
        return False
     except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
