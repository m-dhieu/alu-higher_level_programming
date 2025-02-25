#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    try:
        for i in range(1, a+1):
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
    except Exception:
        pass
    finally:
    return int(result)
