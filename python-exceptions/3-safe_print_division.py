#!/usr/bin/python3


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        if result is None:
            print("Inside result: None", end='')
        else:
            print("Inside result: {}".format(result), end='')
        print("\n{} / {} = {}".format(a, b, result))
        return result
