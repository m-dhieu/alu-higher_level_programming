#!/usr/bin/python3


def safe_print_division(a, b):
    result = None
    try:
        print("Inside result: {}".format(a / b))
        result = a / b
    except ZeroDivisionError:
        print("division by zero")
    finally:
        return result
