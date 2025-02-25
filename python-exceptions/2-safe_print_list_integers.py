#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    try:
        while i < x:
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end='')
                count += 1
            i += 1
        print()
        return count
    except IndexError:
        raise IndexError("list index out of range")
