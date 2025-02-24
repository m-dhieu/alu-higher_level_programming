#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    list_length = 0
    try:
        while True:
            my_list[list_length]
            list_length += 1
    except IndexError:
        pass

    if x > list_length:
        raise IndexError("x is bigger than the length of my_list")

    printed = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=" ")
                printed += 1
    finally:
        print()
        return printed
